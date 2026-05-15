{% test coordinates_valid(model, column_name) %}
    SELECT
        {{ column_name }}
    FROM
        {{ model }}
    WHERE {{ column_name }} IS NULL
        OR pg_typeof({{ column_name }})::text != 'point'
        OR {{ column_name }}[0] NOT BETWEEN -180 AND 180
        OR {{ column_name }}[1] NOT BETWEEN -90 AND 90
{% endtest %}
