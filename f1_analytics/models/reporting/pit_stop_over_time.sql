-- This model:
-- 1) finds the average pit stops times by race by constructor (post 2014)
-- note: filtering out large outliers (> 5 min stops) since many of these are retirements/race incidents
-- 2) ranking the constructors avg stop by year by race
-- 3) calculating the average rank over a season

with stop_avg_by_race as (
	select
		year,
		race_id,
		constructor_id,
		round(avg(time_s), 3) as stop_time_avg
	from {{ ref('stg_pit_stop') }}
	where year >= 2014
		and time_s < 300
	group by all
),
stop_rank_by_race as (
	select
		year,
		constructor_id,
		rank() over(partition by race_id order by stop_time_avg) as race_rank
	from stop_avg_by_race
)
select
	year::varchar as year,
	constructor_id,
	round(avg(race_rank), 2) as season_rank_avg
from stop_rank_by_race
group by all
