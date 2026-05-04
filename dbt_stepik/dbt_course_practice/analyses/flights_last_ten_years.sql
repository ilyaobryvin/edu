{% set current_date = run_started_at|string|truncate(10, True, "") -%}
{% set current_year = current_date[0:4]|int -%}
{% set prev_year = current_year - 10 -%}
{% set prev_date = prev_year|string ~ current_date[4:10] -%}

select
    count(*) as flights_count
from {{ ref('fct_flights') }}
where scheduled_departure between '{{ prev_date }}' and '{{ current_date }}'
