{% macro count_dbt_models() %}

    {% set dct_all_models = {"model":[], "seed":[], "snapshot":[]} %}

    {% for node in graph.nodes.values() %}
    
        {% if node.resource_type == 'model' %}
            {% do dct_all_models["model"].append(node.unique_id) %}
        {% elif node.resource_type == 'seed' %}
            {% do dct_all_models["seed"].append(node.unique_id) %}
        {% elif node.resource_type == 'snapshot' %}
            {% do dct_all_models["snapshot"].append(node.unique_id) %}
        {% endif %}
    
    {% endfor %}

    {% do log('Всего в проекте:', info=true) %}
    {% for k,v in dct_all_models.items() %}
        {% do log('  - ' ~ v | length ~ ' ' ~ k ~ "'s", true)%}
    {% endfor %}

{#
    {% do log(dct_all_models, info=true) %}
#}
{%endmacro%}