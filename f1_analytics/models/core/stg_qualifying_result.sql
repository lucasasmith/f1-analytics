{{ config(alias='qualifying_result') }}

with source as (
    select *
    from
        {{ source("f1_raw", "races_qualifying_results") }}
)

select
    raceId as race_id,
    driverId as driver_id,
    constructorId as constructor_id,
    positionDisplayOrder as position,
    q1Millis as q1_ms,
    q2Millis as q2_ms,
    q3Millis as q3_ms,
    timeMillis as time_ms, -- Used for pre-current era races.
    laps,
    year
from
    source
