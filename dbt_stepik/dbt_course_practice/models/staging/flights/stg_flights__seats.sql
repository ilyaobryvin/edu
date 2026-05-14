{{
    config(
        materialized = 'table'
    )
}}

select 
    aircraft_code,
    seat_no,
    fare_conditions,
    'static_value' as static_field
from {{ source('demo_src', 'seats') }}
