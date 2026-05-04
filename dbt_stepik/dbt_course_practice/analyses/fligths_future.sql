select 
    date(scheduled_departure) as scheduled_departure,
    count(*) as rows
from {{ ref('fct_flights') }}
where scheduled_departure >= '{{ run_started_at|string|truncate(10, True, "") }}'
group by 1