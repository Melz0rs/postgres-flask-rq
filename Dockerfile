FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN mkdir -p app

COPY . /app

WORKDIR /app

EXPOSE 5000

RUN pip3 install -r requirements.txt

CMD ["python3", "api.py"]
