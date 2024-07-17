FROM python:3.11-slim-buster

WORKDIR /app
COPY requirements.txt /imageGenerate/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /imageGenerate/requirements.txt
COPY . /imageGenerate
CMD ["sh", "-c","python3 app/main.py"]
