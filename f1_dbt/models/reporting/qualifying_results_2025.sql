-- Calculate qualifying performance.

select
    concat(format('{:02d}', race.round), '-', race.gp_id) as race_desc,
    qr.driver_id,
    qr.constructor_id,
    qr.position,
    case
        when qr.q3_ms is not null then q3_ms
        when qr.q2_ms is not null then q2_ms
        when qr.q1_ms is not null then q1_ms
        else null
    end as final_time,
    case
        when qr.q3_ms is not null then 'q3'
        when qr.q2_ms is not null then 'q2'
        when qr.q1_ms is not null then 'q1'
        else 'non-participant'
    end as farthest_round
from
    {{ ref('stg_qualifying_result') }} as qr
    inner join {{ ref('stg_race') }} as race
    using(race_id)
where
    qr.year = {{ var('current_season_year') }}
