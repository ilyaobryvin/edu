{% test airport_code_pattern(model, column_name)%}
    select
        {{ column_name }}
    from {{ model }}
    where length({{ column_name }}) != 3
        OR {{ column_name }} != UPPER({{ column_name }}) 
{%endtest%}