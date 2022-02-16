FROM python:3.7

RUN mkdir /api-server
WORKDIR /api-server
ADD . /api-server/
RUN pip install -r requirements.txt

EXPOSE 30000
CMD ["python", "/api-server/api_server.py"]