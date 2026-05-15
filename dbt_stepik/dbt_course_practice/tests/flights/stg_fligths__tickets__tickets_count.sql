{{
    config(
        error_if='>100',
        warn_if='>=50'
    )
}}

with tickets as (
    select
        book_ref,
        count(ticket_no) as cnt_tickets
    from {{ref('stg_flights__tickets')}}
    group by 1 
)
select
    book_ref,
    cnt_tickets
from tickets where cnt_tickets >= 5