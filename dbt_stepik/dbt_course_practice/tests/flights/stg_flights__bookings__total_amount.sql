select 
    total_amount
from {{ ref('stg_flights__bookings') }}
where total_amount <= 0 or total_amount > 10000000