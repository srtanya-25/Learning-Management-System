FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "drf_project/manage.py", "runserver", "0.0.0.0:8000"]