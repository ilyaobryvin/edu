{% snapshot dim_flights__seats %}

{{
    config(
        target_schema='snapshot',
        unique_key='aircraft_code',
        strategy='check',
        check_cols=['seat_no','fare_conditions'],
        dbt_valid_to_current="'5999-01-01'"
    )
}}

select
    aircraft_code,
    seat_no,
    fare_conditions
from {{ ref("stg_flights__seats") }}

{% endsnapshot %}