# Use an official Python image
FROM python:3.12.8

# Set the working directory in the container
WORKDIR /app

# Copy the script and the CSV file into the container
COPY ingest_data.py ingest_data.py
COPY taxi_zone_lookup.csv taxi_zone_lookup.csv

# Install dependencies (including dotenv)
RUN pip install pandas sqlalchemy psycopg2 python-dotenv

# Run the script when the container starts
ENTRYPOINT [ "python", "ingest_data.py" ]

# Expose the port the app runs on
EXPOSE 80


# docker build -t ingest_data:vxxx .
# docker run --env-file .env --network="host" ingest_data



# docker run -it \
#     -e POSTGRES_USER="root" \
#     -e POSTGRES_PASSWORD="root" \
#     -e POSTGRES_DB="ny_taxi" \
#     -v $(pwd)/ny_taxi_data:/var/lib/postgresql/data \
#     -p 5432:5432 \
#     postgres:13

# docker run -it \
#   -e POSTGRES_USER="root" \
#   -e POSTGRES_PASSWORD="root" \
#   -e POSTGRES_DB="ny_taxi" \
#   -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
#   -p 5432:5432 \
#   --network=pg-network \
#   --name pg-database \
#   postgres:13

# docker run -it \
#   -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
#   -e PGADMIN_DEFAULT_PASSWORD="root" \
#   -p 8080:80 \
#   --network=pg-network \
#   --name pgadmin-2 \
#   dpage/pgadmin4