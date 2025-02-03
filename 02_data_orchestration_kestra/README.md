# Data Orchestration HW - M2, W2

## Q1.

File Size:

- 128.3 MB
- 134.5 MB
- 364.7 MB
- 692.6 MB

ANSWER --> 128.3 MB


## Q2.
What is the rendered value of the variable `file` when the inputs `taxi` is set to `green`, `year` is set to `2020`, and `month` is set to `04` during execution?
- `{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv` 
- `green_tripdata_2020-04.csv`
- `green_tripdata_04_2020.csv`
- `green_tripdata_2020.csv`

ANSWER --> `{green_tripdata_2020-04.csv}`


## Q3. 
Rows for  `Yellow Taxi Data` in the whole 2020?
- 13,537.299
- 24,648,499
- 18,324,219
- 29,430,127

--> ANSWER 24,648,499


## Q4.
Rows for the `Green Taxi Data` in the whole 2020?
- 5,327,301
- 936,199
- 1,734,051
- 1,342,034

ANSWER --> 1,734,051


## Q5.
Amount of rows for the `Yellow Taxi Data` for March 2021?
- 1,428,092
- 706,911
- 1,925,152
- 2,561,031

ANSWER --> 1,925,152


## Q6.
Configure the timezone to New York?
- Add a `timezone` property set to `EST` in the `Schedule` trigger configuration  
- Add a `timezone` property set to `America/New_York` in the `Schedule` trigger configuration
- Add a `timezone` property set to `UTC-5` in the `Schedule` trigger configuration
- Add a `location` property set to `New_York` in the `Schedule` trigger configuration  

ANSWER --> `America/New_York`

```md
    triggers:
      - id: daily-schedule
        type: io.kestra.core.models.triggers.types.Schedule
        cron: "0 9 * * *"  # Runs every day at 9 AM
        timezone: "America/New_York"