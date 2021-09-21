FROM python:3.9

WORKDIR /opt/electric

COPY . .

RUN pip install --no-cache-dir -r requirements-production.txt

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]