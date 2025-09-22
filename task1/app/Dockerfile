FROM python:3.11-slim

# set workdir
WORKDIR /app

# install system deps for psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# copy and install python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY . .

# expose port used by the app
EXPOSE 5000

# healthcheck used by container runtime
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

CMD ["python", "app.py"]

