#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
from time import time
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Ingest CSV data into Postgres database using pandas and sqlalchemy
def main():
    
    load_dotenv()

    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')
    db = os.getenv('POSTGRES_DB')
    green_tripdata_table_name = os.getenv('POSTGRES_TABLE_NAME_GREEN_TRIPDATA')
    taxi_zone_lookup_table_name = os.getenv('POSTGRES_TABLE_NAME_ZONE_LOOKUP')
    csv_trips = os.getenv('CSV_GREEN_TRIPDATA')
    csv_zones = os.getenv('CSV_TAXI_ZONE_LOOKUP')


    # create a conn to the DB with sqlalchemy and psycopg2
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}')


    # read the TAXI_ZONE lookup data and create {the taxi_zone_lookup} table
    df_zones = pd.read_csv(csv_zones)
    df_zones.to_sql(name=taxi_zone_lookup_table_name, con=engine, if_exists='replace')

    # insert the data into the table in the Postgres database
    df_iter = pd.read_csv(csv_trips, iterator=True, chunksize=100000, dtype={"store_and_fwd_flag": str})
    
    df = pd.read_csv(csv_trips, nrows=100)
    df = next(df_iter)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.head(n=0).to_sql(name=green_tripdata_table_name, con=engine, if_exists='replace')

    # insert the data in chunks into the table in Postgres database
    for df in df_iter:
        t_start = time()
        
        # convert to datetime format for the timestamp columns in the data
        df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
        df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
        
        # insert the data into the table in the Postgres database
        df.to_sql(name=green_tripdata_table_name, con=engine, if_exists='append', index=False)

        t_end = time()

        print('inserted another chunk, took %.3f second' % (t_end - t_start))
    
# end of main function

if __name__ == '__main__':
    main()
