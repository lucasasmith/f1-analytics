{{ config(alias='circuits') }}

with source as (
    select *
    from
        {{ source("f1_raw", "circuits") }}
)

select
    circuitID as circuit_id,
    circuitRef as circuit_ref_name,
    name,
    location as location_name,
    case country
        when 'United States' then 'USA'
        else country
    end as country,
    lat as latitude,
    lng as longitude,
    alt as altitude,
    url
from
    source
