FROM python:3.11

WORKDIR /app

RUN pip install boto3

COPY upload_to_s3.py /app/
COPY var_ambientes.py /app/
COPY movies.csv /app/
COPY series.csv /app/

VOLUME /app

CMD ["python", "upload_to_s3.py"]