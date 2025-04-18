
select
    concat(format('{:02d}', race.round), '-', race.gp_id) as race_desc,
    rr.driver_id,
    rr.position
from
    {{ ref('stg_race_result') }} as rr
    inner join {{ ref('stg_race') }} as race
    using(race_id)
where
    rr.year = extract('year' from today())
