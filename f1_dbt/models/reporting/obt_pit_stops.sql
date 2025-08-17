-- This is a "One Big Table" representation of the pit stops dimensional model.
-- This table would be redundant with a proper BI setup in Tableu/Looker/etc.

with fct_pit_stops as (
    select *
    from {{ ref('fct_pit_stops') }}
),

dim_constructors as (
    select *
    from {{ ref('dim_constructors') }}    
),

dim_drivers as (
    select *
    from {{ ref('dim_drivers') }}    
),

dim_races as (
    select *
    from {{ ref('dim_races') }}
),

dim_tyre_manufacturers as (
    select *
    from {{ ref('dim_tyre_manufacturers') }}
)

-- Exclude the surrogate keys since they're only utilized for the joins.
select
    fct_pit_stops.* exclude(race_id, constructor_id, driver_id, tyre_manufacturer_id),
    dim_constructors.name as constructor_name,
    dim_races.year as race_year,
    dim_races.official_name as race_title,
    dim_drivers.name as driver_name,
    dim_tyre_manufacturers.name as tyre_manufacturer_name
from
    fct_pit_stops
    left join dim_constructors
        on fct_pit_stops.constructor_id = dim_constructors.constructor_id
    left join dim_races
        on fct_pit_stops.race_id = dim_races.race_id
    left join dim_drivers
        on fct_pit_stops.driver_id = dim_drivers.driver_id
    left join dim_tyre_manufacturers
        on fct_pit_stops.tyre_manufacturer_id = dim_tyre_manufacturers.tyre_manufacturer_id
