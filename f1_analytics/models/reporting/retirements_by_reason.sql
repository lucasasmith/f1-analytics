
select
    lower(reason_retired) reason_retired,
    count(0) as count
from
    {{ ref('stg_race_result') }}
where
    reason_retired is not null
group by
    all
having
    count >= 5 -- This is to help remove abnormal reasons.
