{{ config(alias='drivers') }}

with source as (
    select *
    from
        {{ source("f1_raw", "drivers") }}
)

select
    driverId as driver_id,
    driverRef as driver_ref_name,
    nullif(number, '\N')::int as number,
    code,
    forename as first_name,
    surname as last_name,
    dob,
    case nationality
        when 'East German' then 'German'
        else nationality
    end as nationality,
    url
from
    source
