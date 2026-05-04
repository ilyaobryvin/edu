{{
    config(
        materialized = 'table',
        post_hook="
            {% set current_datetime = run_started_at.strftime('%Y%m%d_%H%M%S') %}

            {% set backup_relation = api.Relation.create(
                database = this.database,
                schema = this.schema,
                identifier = this.identifier ~ '_' ~ current_datetime,
                type = 'table'
            )
            %}

            {% do adapter.rename_relation(this, backup_relation) %}
        "
    )
}}

select 
    aircraft_code,
    model,
    "range"
from {{ source('demo_src', 'aircrafts') }}