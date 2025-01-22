-- Find the most recent race for each circuit.
select
    circuits.name as circuit_name,
    race.name as race_name,
    race.date,
    race.url
from
    {{ ref('stg_races') }} as race
    inner join {{ ref('stg_circuits') }} as circuits
    on race.circuit_id = circuits.circuit_id
qualify
    row_number() over(partition by race.circuit_id order by race.date desc) = 1
