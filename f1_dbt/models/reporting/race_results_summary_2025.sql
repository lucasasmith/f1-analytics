-- Calculate the summary statistics for each driver for the season.

select
    rr.driver_id,
    round(avg(rr.position), 1) as avg_result,
    min(rr.position) as best_result,
    max(rr.position) as worst_result,
    count(rr.position) as total_races
from
    {{ ref('stg_race_result') }} as rr
    inner join {{ ref('stg_race') }} as race
    using(race_id)
where
    rr.year = 2025
    and rr.position is not null
group by
    all
