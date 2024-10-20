FROM python:latest

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=nutrient.py

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]