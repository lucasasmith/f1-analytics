with results as (
    select
        qr.race_id,
        concat(format('{:02d}', race.round), '-', race.gp_id) as race_desc,
        qr.driver_id,
        qr.position,
        sum(qr.position) over(partition by qr.driver_id order by qr.race_id) as total_position_value,
        count(qr.race_id) over(partition by qr.driver_id order by qr.race_id) as accum_event_participated,
        count(qr.race_id) over(partition by qr.driver_id) as total_participated
    from
        {{ ref('stg_qualifying_result') }} as qr
        inner join {{ ref('stg_race') }} as race
        using(race_id)
    where
        qr.year = {{ var('current_season_year') }}
        and qr.position is not null
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
