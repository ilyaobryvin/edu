{% macro check_dependencies(node) %}

    {% if execute %}
        {% set depends_on = node.get('depends_on', {}) %}
        {% set dependency_nodes = depends_on.get('nodes', []) %}
        {% set dependency_macros = depends_on.get('macros', []) %}
        {% set dependencies_count = (dependency_nodes | length) + (dependency_macros | length) %}

        {% do log("⚠️  Модель " ~ node.name ~ " зависит от " ~ dependencies_count ~ " объектов!", info=true) %}
    {% endif %}

{% endmacro %}
