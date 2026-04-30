{% snapshot dim_flights__aircrafts %}

{{
    config(
        target_schema='snapshot',
        unique_key='aircraft_code',
        strategy='check',
        check_cols=['model','range'],
        dbt_valid_to_current="'5999-01-01'"
    )
}}

select
    aircraft_code,
    model,
    "range"
from {{ ref("stg_flights__aircrafts") }}

{% endsnapshot %}