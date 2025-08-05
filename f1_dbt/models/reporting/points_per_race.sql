select distinct
    driver_id,
    count(distinct race_id) over(partition by driver_id)  as total_races,
    sum(points) over(partition by driver_id) as total_points,
    sum(points) over(partition by driver_id) / count(distinct race_id) over(partition by driver_id) as avg_points_per_race
    -- add in last race date
from
    {{ ref('stg_race_result') }}
order by
    avg_points_per_race
