select
    aircraft_code,
    count(seat_no) as seats
from {{ref('stg_flights__seats')}}
group by 1 
