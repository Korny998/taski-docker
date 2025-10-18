FROM python:3.12

WORKDIR /app

RUN pip install gunicorn==23.0.0

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir --no-build-isolation -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]