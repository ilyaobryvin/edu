{{
    config(
     materialized = 'incremental',
     incremental_strategy = 'append',
     tags = ['bookings']
    )
}}

select
    {{-bookref_to_bigint('book_ref')}} as book_ref,
    book_date,
    {{-kopeck_to_ruble(column_name = 'total_amount')}} as total_amount
from {{ source('demo_src', 'bookings') }}
{% if is_incremental() %}
where
    {{-bookref_to_bigint('book_ref')}} > (SELECT MAX({{-bookref_to_bigint('book_ref')}}) FROM {{ this }})
{% endif %}