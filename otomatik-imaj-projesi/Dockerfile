FROM python:3.12-slim
WORKDIR /app

# Bagimlilik listesi koddan once kopyalanir; kod degisince pip install onbellegi bozulmasin.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
EXPOSE 8000
CMD ["python", "app.py"]
