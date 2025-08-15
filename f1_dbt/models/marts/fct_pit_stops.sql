-- Fact table for the purpose of observing pit stops and their time duration in seconds.

select
    {{ dbt_utils.generate_surrogate_key(['race_id', 'constructor_id', 'stop']) }} as pit_stop_id,
    {{ dbt_utils.generate_surrogate_key(['race_id']) }} as race_id,
    {{ dbt_utils.generate_surrogate_key(['constructor_id']) }} as constructor_id,
    ps.stop,
    ps.time_s as time_s,
from
    {{ ref('stg_pit_stop') }} as ps
