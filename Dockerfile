
FROM python:3.12-slim

WORKDIR /app

COPY otomatik-imaj-projesi/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY otomatik-imaj-projesi/app.py ./app.py

EXPOSE 8000

CMD ["python", "app.py"]
