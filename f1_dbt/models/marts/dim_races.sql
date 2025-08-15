
select
    {{ dbt_utils.generate_surrogate_key(['race_id']) }} as race_id,
    official_name,
    year
from {{ ref('stg_race') }}
