FROM python:3.11-slim

WORKDIR /app

COPY wheels/ /wheels/
COPY requirements.txt .
RUN pip install --no-index --find-links=/wheels -r requirements.txt

COPY app/ ./app/
COPY download_model.py .
COPY main.py .
COPY persona.json .

CMD ["python", "main.py"]
