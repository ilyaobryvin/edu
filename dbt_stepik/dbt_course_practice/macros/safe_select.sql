{% macro safe_select(table_name) %}
    {% if execute %}

        {% set database = target.database %}
        {% set schema = target.schema %}

        {#
            relation для модели/таблицы, имя которой передали в table_name.
        #}
            {% set source_relation = adapter.get_relation(
                database=database,
                schema=schema,
                identifier=table_name) -%}
            {% do log("Source Relation: " ~ source_relation, info=true) %}

        {#
            После получения relation нужно проверить, существует ли таблица:
        #}
            {% if source_relation %}
                select * from {{ source_relation }}
            {% else %}
                select null
            {% endif %}

    {% endif %}
{% endmacro %}
