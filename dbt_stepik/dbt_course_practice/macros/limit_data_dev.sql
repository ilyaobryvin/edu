{% macro limit_data_dev(column_name, days=5000) %}
    {% if target.name == 'dev' and days < 0 %}
        {{ exceptions.raise_compiler_error("Invalid 'days'. Got: " ~ days) }}
    {% elif target.name == 'dev' %}
WHERE {{ column_name -}} >= {{- dbt.dateadd(datepart="day", interval=-days, from_date_or_timestamp="current_date") -}}
    {% endif %}
{% endmacro %}
