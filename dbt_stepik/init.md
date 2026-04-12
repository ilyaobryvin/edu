uv venv --python 3.13

uv pip install dbt-core
uv pip install dbt-postgres
dbt init dbt_scooters (с активированной средой)

uv run dbt --version
uv run dbt debug

<!-- альтернативный способ создания проекта чем venv. Лучше использовать его.
Виртуальное окржение создается после команды uv add -->
uv init --bare
uv add dbt-postgres
uv run dbt debug (без venv activate)