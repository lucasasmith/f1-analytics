{{ config(alias='pit_stop') }}

with source as (
    select *
    from
        {{ source("f1_raw", "races_pit_stops") }}
)

select
    raceId as race_id,
    constructorId as constructor_id,
    driverId as driver_id,
    stop,
    md5(concat(raceId, constructor_id, driver_id, stop)) as pit_stop_id, -- Creating the pk
    year,
    round,
    lap,
    timeMillis / 1000 as time_s
from
    source
