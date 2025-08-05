
select
    {{ dbt_utils.generate_surrogate_key(['circuit_id']) }} as circuit_id,
    name,
    country_id as country,
    type
from {{ ref('stg_circuit') }}
