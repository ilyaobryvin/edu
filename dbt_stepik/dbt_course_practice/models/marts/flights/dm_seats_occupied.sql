{{
    config(
        materialized='table'
    )
}}

with flights as (
    select * from {{ ref('fct_flights') }}
),
airports as (
    select * from {{ ref('stg_flights__airports') }}
),
aircrafts as (
    select * from {{ ref('stg_flights__aircrafts') }}
),
ticket_flights as (
    select * from {{ ref('fct_ticket_flights') }}
),
boarding_passes as (
    select * from {{ ref('fct_boarding_passes') }}
),
seats as (
    select * from {{ ref('stg_flights__seats') }}
),
ticket_flights_agg as (
    select
        flight_id,
        count(ticket_no) as ticket_flights_purchased,
        sum(amount) as ticket_flights_amount
    from ticket_flights
    group by flight_id
),
boarding_passes_agg as (
    select
        flight_id,
        count(ticket_no) as boarding_passes_issued
    from boarding_passes
    group by flight_id
),
seats_agg as (
    select
        aircraft_code,
        count(seat_no) as seats_total
    from seats
    group by aircraft_code
)
select
    departure_airports.airport_code as departure_airport_code,
    departure_airports.airport_name as departure_airport_name,
    departure_airports.city as departure_airport_city,
    departure_airports.coordinates as departure_airport_coordinates,
    arrival_airports.airport_code as arrival_airport_code,
    arrival_airports.city as arrival_airport_city,
    arrival_airports.airport_name as arrival_airport_name,
    arrival_airports.coordinates as arrival_airport_coordinates,
    flights.status as flight_status,
    flights.aircraft_code,
    aircrafts.model as aircraft_model,
    cast(flights.scheduled_departure as date) as scheduled_departure_date,
    flights.flight_no,
    flights.flight_id,
    coalesce(ticket_flights_agg.ticket_flights_purchased, 0) as ticket_flights_purchased,
    coalesce(boarding_passes_agg.boarding_passes_issued, 0) as boarding_passes_issued,
    coalesce(ticket_flights_agg.ticket_flights_amount, 0) as ticket_flights_amount,
    coalesce(seats_agg.seats_total, 0)
        - coalesce(ticket_flights_agg.ticket_flights_purchased, 0) as ticket_flights_no_sold
from flights
left join airports as departure_airports
    on flights.departure_airport = departure_airports.airport_code
left join airports as arrival_airports
    on flights.arrival_airport = arrival_airports.airport_code
left join aircrafts
    on flights.aircraft_code = aircrafts.aircraft_code
left join ticket_flights_agg
    on flights.flight_id = ticket_flights_agg.flight_id
left join boarding_passes_agg
    on flights.flight_id = boarding_passes_agg.flight_id
left join seats_agg
    on flights.aircraft_code = seats_agg.aircraft_code
