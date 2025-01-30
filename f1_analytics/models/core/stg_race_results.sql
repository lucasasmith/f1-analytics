{{ config(alias='race_results') }}

with source as (
    select *
    from
        {{ source("f1_raw", "races_race_results") }}
)

select
    raceId as race_id,
    driverId as driver_id,
    constructorId as constructor_id,
    engineManufacturerId as engine_manufacturer_id,
    time,
    timeMillis as time_ms,
    timePenalty as time_penalty,
    timePenaltyMillis as time_penalty_ms,
    gap,
    gapMillis as gap_ms,
    gapLaps as gap_laps,
    interval,
    intervalMillis as interval_ms,
    reasonRetired as reason_retired,
    points,
    pitStops as pit_stops,
    driverOfTheDay as is_driver_of_the_day,
from
    source
