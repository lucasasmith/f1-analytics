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

dim_races as (
    select *
    from {{ ref('dim_races') }}
)

-- Exclude the surrogate keys since they're only utilized for the joins.
select
    fct_pit_stops.* exclude(race_id, constructor_id),
    dim_constructors.* exclude(constructor_id),
    dim_races.* exclude(race_id)
from
    fct_pit_stops
    left join dim_constructors
        on fct_pit_stops.constructor_id = dim_constructors.constructor_id
    left join dim_races
        on fct_pit_stops.race_id = dim_races.race_id
