{{ config(alias='race') }}

with source as (
    select *
    from
        {{ source("f1_raw", "races") }}
)

select
    id as race_id,
    year,
    round,
    date,
    time,
    grandPrixId as gp_id,
    officialName as official_name,
    circuitID as circuit_id,
    qualifyingFormat as qualifying_format,
    sprintQualifyingFormat as sprint_qualifying_format,
    laps,
    qualifyingDate as qualifying_date,
    qualifyingTime as qualifying_time
from
    source
