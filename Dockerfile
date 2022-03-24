FROM python:alpine3.14
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "rest-api.py"]