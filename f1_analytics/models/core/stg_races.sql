{{ config(alias='races') }}

with source as (
    select *
    from
        {{ source("f1_raw", "races") }}
)

select
    raceId as race_id,
    year,
    round,
    circuitID as circuit_id,
    name,
    date,
    time,
    url,
    quali_time as qualifying_time,
    sprint_date,
    sprint_time
from
    source
