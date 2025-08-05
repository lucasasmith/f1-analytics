{{ config(alias='circuit') }}

with source as (
    select *
    from
        {{ source("f1_raw", "circuits") }}
)

select
    id as circuit_id,
    name,
    fullName as full_name,
    placeName as place_name,
    lower(type) as type,
    direction,
    countryId as country_id,
    latitude,
    longitude,
    length as length_km,
    turns
from
    source
