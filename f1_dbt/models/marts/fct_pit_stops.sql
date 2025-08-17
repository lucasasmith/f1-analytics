-- Fact table for the purpose of observing pit stops and their time duration in seconds.

select
    {{ dbt_utils.generate_surrogate_key(['race_id', 'constructor_id', 'stop_num']) }} as pit_stop_id,
    {{ dbt_utils.generate_surrogate_key(['race_id']) }} as race_id,
    {{ dbt_utils.generate_surrogate_key(['constructor_id']) }} as constructor_id,
    {{ dbt_utils.generate_surrogate_key(['driver_id']) }} as driver_id,
    {{ dbt_utils.generate_surrogate_key(['tyre_manufacturer_id']) }} as tyre_manufacturer_id,
    ps.stop_num,
    ps.time_s
from
    {{ ref('stg_pit_stop') }} as ps
