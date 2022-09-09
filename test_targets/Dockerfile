FROM python:3.7.2-stretch

WORKDIR /application/

COPY Pipfile Pipfile.lock run_targets.sh send_requests.sh /application/
COPY src /application/src

RUN apt-get update
RUN apt-get -y install lsof curl
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --deploy --system

ENV PYTHONPATH=/application

RUN chmod u+x /application/run_targets.sh
RUN chmod u+x /application/send_requests.sh

CMD ["/application/run_targets.sh"]
