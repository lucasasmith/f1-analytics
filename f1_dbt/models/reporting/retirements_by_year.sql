
select
    race.year,
    count(0) as retirement_count
from
    {{ ref('stg_race_result') }} as rr
    inner join {{ ref('stg_race') }} as race
    using(race_id)
where
    rr.reason_retired is not null
group by
    all
