## Question 1. Question 1. Understanding docker first run
command: pip --version

## Question 3. Trip Segmentation Count
```sql
SELECT
     CASE
         WHEN trip_distance <= 1 THEN 'Up to 1 mile'
         WHEN trip_distance > 1 AND trip_distance <= 3 THEN '1 to 3 miles'
         WHEN trip_distance > 3 AND trip_distance <= 7 THEN '3 to 7 miles'
         WHEN trip_distance > 7 AND trip_distance <= 10 THEN '7 to 10 miles'
         ELSE 'Over 10 miles'
     END AS distance_category,
     COUNT(*) AS trip_count
 FROM
     green_taxi_data
 WHERE
     lpep_pickup_datetime >= '2019-10-01'
     AND lpep_pickup_datetime < '2019-11-01'
 GROUP BY
     distance_category
 ORDER BY
     distance_category;
```

## Question 5. Three biggest pickup zones
```sql
SELECT 
     t."PULocationID" AS pickup_location_id,
     z."Zone" AS pickup_zone,
     z."Borough" AS pickup_borough,
     SUM(t.total_amount) AS total_amount_sum
 FROM 
     green_taxi_data t
 JOIN 
```

## Question 6. Largest tip
```sql
SELECT 
    dz."Zone" AS dropoff_zone,
    MAX(t.tip_amount) AS largest_tip
FROM 
    green_taxi_data t
JOIN 
    taxi_zone_lookup pz
ON 
    t."PULocationID" = pz."LocationID"
JOIN 
    taxi_zone_lookup dz
ON 
    t."DOLocationID" = dz."LocationID"
WHERE 
    pz."Zone" = 'East Harlem North'
    AND t.lpep_pickup_datetime BETWEEN '2019-10-01' AND '2019-11-01'
GROUP BY 
    dz."Zone"
ORDER BY 
    largest_tip DESC
LIMIT 1;
```
