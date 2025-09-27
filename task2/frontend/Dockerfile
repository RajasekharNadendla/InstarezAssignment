FROM python:3.11-slim
WORKDIR /app
COPY index.html .
# Use a very light server to serve static file
RUN pip install --no-cache-dir flask
COPY index.html /app/index.html
CMD ["python", "-m", "http.server", "3000"]
EXPOSE 3000
