{{ config(alias='driver') }}

with source as (
    select *
    from
        {{ source("f1_raw", "drivers") }}
)

select
    id as driver_id,
    name,
    firstName as first_name,
    lastName as last_name,
    fullName as full_name,
    abbreviation,
    dateOfBirth as date_of_birth,
    dateOfDeath as date_of_death,
    placeOfBirth as place_of_birth,
    countryOfBirthCountryId as country_id_of_birth,
    nationalityCountryId as nationality_country_id,
    permanentNumber as number
from
    source
