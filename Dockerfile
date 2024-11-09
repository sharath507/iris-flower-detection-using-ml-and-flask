FROM python:3.11

WORKDIR /code

COPY ./requirements.txt .

RUN pip install --upgrade pip


RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . .

EXPOSE 8000

CMD ["python","app.py"]