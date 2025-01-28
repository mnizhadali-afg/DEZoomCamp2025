FROM python:3.12.8

RUN pip install pandas

WORKDIR /app
COPY pipeline.py pipeline.py

ENTRYPOINT [ "python", "pipeline.py" ]

# docker run -it \
#     -e POSTGRES_USER="root" \
#     -e POSTGRES_PASSWORD="root" \
#     -e POSTGRES_DB="ny_taxi" \
#     -v $(pwd)/ny_taxi_data:/var/lib/postgresql/data \
#     -p 5432:5432 \
#     postgres:13