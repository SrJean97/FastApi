FROM python:3.10.7

RUN pip install fastapi uvicorn 

#EXPOSE 80

COPY ./app /app

#WORKDIR /code

#RUN pip update

#RUN pip install python3 -y

#COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]






