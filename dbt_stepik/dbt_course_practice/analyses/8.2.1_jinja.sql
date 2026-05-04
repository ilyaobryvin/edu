{% set flights_relation = adapter.get_relation(
    database='dwh_flight',
    schema='intermediate',
    identifier='stg_flights__flights'
    )
%}

{{ 'database: ' ~ flights_relation.database }}
{{ 'schema: ' ~ flights_relation.schema }}
{{ 'identifier: ' ~ flights_relation.identifier }}
{{ 'is_table: ' ~ flights_relation.is_table }}
{{ 'database: ' ~ flights_relation.database }}

{% set flights_relation = load_relation(
    ref('stg_flights__flights')
    )
%}

{% set columns = adapter.get_columns_in_relation(
    flights_relation) 
%}

{% for column in columns -%}
    {{ 'Columns :' ~ column }}
{% endfor %}

