with season_avg_position as (
	select
	    year,
	    driver_id,
	    round(avg(position), 3) as season_avg_position
	from
	    {{ ref('stg_race_result') }}
	group by
		all
	having
		count(distinct race_id) > 10
)
select 
	year::varchar as year,
	driver_id,
	season_avg_position,
	rank() over(order by season_avg_position) as rank
from
	season_avg_position
qualify
	rank <= 100 -- Top 100 only.
