

FROM python:3.12-slim

WORKDIR /app

COPY otomatik-imaj-projesi/gereksinimler.txt .
RUN pip install --no-cache-dir -r gereksinimler.txt

COPY otomatik-imaj-projesi/uygulama.py ./uygulama.py

EXPOSE 8000

CMD ["python", "uygulama.py"]
