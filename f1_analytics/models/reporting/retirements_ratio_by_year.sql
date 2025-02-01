
select
    race.year,
    round(count(rr.reason_retired) /
    count(distinct race.race_id), 1) as ratio
from
    {{ ref('stg_race_result') }} as rr
    inner join {{ ref('stg_race') }} as race
    using(race_id)
group by
    all
