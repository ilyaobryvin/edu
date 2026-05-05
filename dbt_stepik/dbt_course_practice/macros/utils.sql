{% macro show_columns_relation(table_name) %}
    {%- if execute -%}

        {%- set database = target.database -%}
        {%- set schema = target.schema -%}

        {%- set source_relation = adapter.get_relation(
            database=database,
            schema=schema,
            identifier=table_name
        ) -%}

        {%- set columns = adapter.get_columns_in_relation(source_relation) -%}

        {%- for column in columns -%}
            {{column.name}}
                {%-if not loop.last-%},{%-endif-%}
        {%- endfor -%}
    {% else %}
        *
    {%- endif -%}
{% endmacro %}
