FROM python:3.11-slim

WORKDIR /app

# system deps for psycopg2
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Use gunicorn to serve the app on 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2", "--timeout", "30"]
