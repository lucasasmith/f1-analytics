select
    {{ dbt_utils.generate_surrogate_key(['constructor_id']) }} as constructor_id,
    name
from {{ ref('stg_constructors') }}
