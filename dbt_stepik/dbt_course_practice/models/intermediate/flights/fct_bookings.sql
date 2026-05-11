{{
    config(
        materialized='table'
    )
}}

select 
    {{ show_columns_relation('stg_flights__bookings') }}
    , {{ dbt_utils.generate_surrogate_key(['book_ref']) }} as book_ref_key
from {{ ref('stg_flights__bookings') }}
