
{#-  -#}
{#- Пример создания списка для цикла-#}
{%- set flight_statuses = ['Departed', 'On Time'] -%}

{# Сохраняем запрос в переменную jinja #}
{%- set flight_query -%}
select distinct status from {{ ref('stg_flights__flights') }}
{%- endset -%}

{#- Сохраняем результат запроса в переменную -#}
{% set flight_query_result = run_query(flight_query) -%}
    {%- if execute %}
        {%- set flight_statuses = flight_query_result.columns[0] -%}
    {% else %}
        {%- set flight_statuses = [] -%}
    {% endif -%}

select 
    {%- for status in flight_statuses %}
    count(*) filter (where status='{{status}}') as status_{{''.join(status).replace(' ','_')}}
    {%- if not loop.last %},{% endif %}
    {%- endfor %}
from {{ ref('stg_flights__flights') }}