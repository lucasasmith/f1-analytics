
select
    {{ dbt_utils.generate_surrogate_key(['tyre_manufacturer_id']) }} as tyre_manufacturer_id,
    name,
    country_id as country
from {{ ref('stg_tyre_manufacturer') }}
