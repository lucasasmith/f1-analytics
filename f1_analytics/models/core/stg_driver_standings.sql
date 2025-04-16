{{ config(alias='driver_standings') }}

{% set season_year = 2025 %}

with source as (
    select *
    from
        {{ source("f1_raw", "seasons_driver_standings") }}
)

select
    s.driverId as driver_id,
    driver.full_name,
    s.positionNumber as position,
    s.points
from
    source as s
    inner join {{ ref('stg_driver') }} as driver
    on s.driverId = driver.driver_id
where
    year = {{ season_year }}
