with results as (
    select
        rr.race_id,
        concat(format('{:02d}', race.round), '-', race.gp_id) as race_desc,
        rr.driver_id,
        rr.position,
        sum(rr.position) over(partition by rr.driver_id order by rr.race_id) as total_position_value,
        count(rr.race_id) over(partition by rr.driver_id order by rr.race_id) as accum_event_participated,
        count(rr.race_id) over(partition by rr.driver_id) as total_participated
    from
        {{ ref('stg_race_result') }} as rr
        inner join {{ ref('stg_race') }} as race
        using(race_id)
    where
        rr.year = 2024
        and rr.position is not null
)

select
    race_desc,
    driver_id,
    position,
    round(total_position_value / accum_event_participated, 1) as running_avg
from
    results
where
    total_participated > 3
