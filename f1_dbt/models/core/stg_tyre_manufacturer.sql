{{ config(alias='tyre_manufacturer') }}

with source as (
    select *
    from
        {{ source("f1_raw", "tyre_manufacturers") }}
)

select
    id as tyre_manufacturer_id,
    name,
    countryId as country_id
from
    source
