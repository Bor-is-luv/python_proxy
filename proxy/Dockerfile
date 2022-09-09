FROM python:3.7.2-stretch

WORKDIR /application/src

COPY Pipfile Pipfile.lock /application/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --deploy --system

COPY src /application/src

ENV PYTHONPATH=/application
CMD ["python3", "api.py"]
