# app/Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Expose port 5000 inside container
EXPOSE 5000

# Simple health check script uses Flask's /health
HEALTHCHECK --interval=10s --timeout=3s --retries=5 \
  CMD curl -f http://127.0.0.1:5000/health || exit 1

# Run with gunicorn for a production-like server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2"]
