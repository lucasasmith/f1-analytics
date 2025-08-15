{{ config(alias='constructors') }}

with source as (
    select *
    from
        {{ source("f1_raw", "constructors") }}
)

select
    id as constructor_id,
    name,
    fullName as full_name,
    countryId as country_id
from
    source
