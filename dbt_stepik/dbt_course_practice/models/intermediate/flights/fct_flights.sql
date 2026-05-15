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
    actual_arrival,
    
    case
        when actual_departure is not null and scheduled_departure < actual_departure
        then actual_departure - scheduled_departure
        else INTERVAL '0 seconds'
    end as flight_departure_delay,

    case
        when actual_departure is not null and actual_arrival is not null
        then actual_arrival - actual_departure
        else INTERVAL '0 seconds'
    end as actual_duration_flight
from {{ ref('stg_flights__flights') }}
