{{
    config(
        materialized='table',
        post_hook="
            {% if execute %}
                {% set statuses = dbt_utils.get_column_values(
                    table=this,
                    column='status'
                ) %}
                
                {% do log('Актуальные статусы:', info=true) %}
                {% for status in statuses %}
                    {% do log('- ' ~ status, info=true) %}
                {% endfor %}
            {% endif %}

            select 1
        "
    )
}}

select 
    flight_id,
    flight_no,
    scheduled_departure,
    scheduled_arrival,
    departure_airport,
    arrival_airport,
    status,
    aircraft_code,
    actual_departure,
    actual_arrival
from {{ ref('stg_flights__flights') }}
