from fastapi import FastAPI, Response, Depends, HTTPException, Security, Request
from fastapi.security.api_key import APIKeyQuery
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn
import httpx
from aredis import StrictRedis


from src.settings import (REDIS_HOST, REDIS_PORT, TARGETS_ADDRESSES, REDIS_KEYS)
from src.logs import LOGGER

async_redis_client = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

http_async_client = httpx.AsyncClient(timeout=None)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/healthcheck')
async def healthcheck():
    return HTMLResponse('<h3>Is running', 200)
    

@app.api_route('/', methods=['POST', 'GET', 'PUT', 'DELETE', 'OPTIONS', 'PATCH'])
async def proxy(request: Request):

    count_handling_requests = await async_redis_client.mget(REDIS_KEYS)
    # LOGGER.info(count_handling_requests)
    count_requests_map = dict(
                          filter(lambda item: item[1] is not None,
                                zip(TARGETS_ADDRESSES, 
                                count_handling_requests)
                                )
                             )
    sorted_count_requests_map = {k: v for k, v in sorted(count_requests_map.items(), 
                                                         key=lambda item: int(item[1]) if item[1] is not None else None)}

    for address, requests_count in sorted_count_requests_map.items():
        if requests_count is not None:
            try:
                response = await http_async_client.request(request.method, 
                                                           address, 
                                                           headers=dict(request.headers.items()),
                                                           data=await request.body())
            except (httpx.RemoteProtocolError, httpx.ReadError, httpx.ConnectError) as e:
                LOGGER.warning(f'{type(e)}: {str(e)} for {address}')
                continue

            if response.status_code == 503:
                pass
            else:
                return HTMLResponse(response.text, response.status_code, response.headers)

    return HTMLResponse('<h3>No working targets</h3>', 503)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)
