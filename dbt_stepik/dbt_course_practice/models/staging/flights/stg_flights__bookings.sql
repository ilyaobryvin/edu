{{
    config(
        materialized='table'
    )
}}

select 
    book_ref,
    book_date,
    {{-bookref_to_bigint('book_ref')}} as book_ref_int, 
    total_amount
from {{ source('demo_src', 'bookings') }}