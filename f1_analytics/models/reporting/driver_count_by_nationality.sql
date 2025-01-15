{{ config(alias='driver_count_by_nationality') }}

select
    nationality,
    count(0) as nationality_count
from
    {{ ref('stg_drivers') }}
group by
    all
