{{
    config(
        materialized = 'view'
    )
}}

{{ safe_select('stg_flights__seats') }}