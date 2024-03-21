FROM python:3.11

WORKDIR /application

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./api api
COPY ./data data
COPY ./templates templates
COPY ./tests tests
COPY ./app.py app.py

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]