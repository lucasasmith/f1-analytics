
select
    {{ dbt_utils.generate_surrogate_key(['driver_id']) }} as driver_id,
    name,
    date_of_birth
from {{ ref('stg_driver') }}
