# DBT Course Practice: как работает проект

## 1. Краткая справка по основным командам dbt

### `dbt debug`
Проверяет, что dbt установлен корректно, видит проект, находит `profiles.yml` и может подключиться к БД по выбранному профилю.

### `dbt parse`
Читает проект, Jinja, YAML, SQL и строит внутренний граф зависимостей, но ничего не создаёт в БД.

### `dbt compile`
Компилирует SQL с учётом `ref()`, `source()`, `config()` и Jinja, но не выполняет запросы на создание таблиц.

### `dbt run`
Строит модели: выполняет SQL-модели и создаёт/обновляет таблицы или view в целевой БД.

### `dbt test`
Запускает тесты качества данных.
В вашем проекте сейчас это source-тесты `not_null` и `unique` для `demo_src.aircrafts.aircraft_code`.

### `dbt build`
Комплексная команда.
Обычно включает в себя построение ресурсов и их проверку: models, tests, seeds, snapshots, source freshness и другие ресурсы, если они есть в проекте и попадают в selection.
В вашем текущем проекте по факту участвуют:
1. 8 моделей
2. 2 source-теста

### `dbt docs generate`
Собирает документацию проекта и артефакты `manifest.json`, `catalog.json` для просмотра lineage и описаний.

### `dbt seed`
Загружает CSV из папки `seeds/` в таблицы БД.
В этом проекте папка есть, но активных seed-файлов сейчас нет.

### `dbt source freshness`
Проверяет, насколько свежи source-таблицы по полю `loaded_at_field` и правилам `warn_after` / `error_after`.


## 2. Что есть в этом проекте

Проект расположен в:

`C:\Users\ilyao\JupyterLab\education\dbt_stepik\dbt_course_practice`

Ключевые части проекта:

1. `dbt_project.yml`
2. `models/staging/flights/*.sql`
3. `models/staging/flights/_flight__source.yml`
4. `models/staging/flights/_fligths__facts__sources.yml`
5. `models/staging/flights/_flights__docs.md`
6. `target/manifest.json`
7. `logs/dbt.log`

В проекте сейчас найдено:

1. 8 моделей
2. 8 source-таблиц
3. 2 теста
4. `postgres` adapter
5. dbt версии `1.11.6`


## 3. Какие конфиги dbt читает и в каком порядке

Когда вы запускаете `dbt build` из корня проекта, порядок логически такой:

1. dbt находит проект по `dbt_project.yml`
2. из `dbt_project.yml` берёт имя профиля: `profile: 'dbt_course_practice'`
3. затем идёт в домашний файл профилей `C:\Users\ilyao\.dbt\profiles.yml`
4. в `profiles.yml` ищет профиль `dbt_course_practice`
5. внутри профиля берёт target `dev`
6. из `outputs.dev` берёт параметры подключения к Postgres
7. после этого читает модели, source-описания, тесты, docs и строит DAG зависимостей
8. затем выполняет SQL в порядке зависимостей

Коротко:

1. `dbt_project.yml` говорит, какой профиль и где искать файлы проекта
2. `profiles.yml` говорит, в какую БД и схему подключаться
3. YAML-файлы в `models/` описывают sources, тесты, freshness, docs
4. SQL-файлы в `models/` описывают, как строить итоговые таблицы


## 4. Какое подключение использует проект

Из `C:\Users\ilyao\.dbt\profiles.yml` для проекта `dbt_course_practice` берутся такие параметры:

1. `type: postgres`
2. `host: localhost`
3. `port: 4001`
4. `user: postgres`
5. `dbname: dwh_flight`
6. `schema: intermediate`
7. `threads: 4`
8. `target: dev`

Пароль в этом описании намеренно не указывается.

Это значит:

1. читать и писать dbt будет в базе `dwh_flight`
2. целевая схема для моделей по умолчанию: `intermediate`
3. параллельность выполнения: до 4 потоков


## 5. Какие БД, схемы и таблицы участвуют

### Источники (`source`)

В YAML-файлах объявлен source с именем `demo_src`.

Поскольку в source YAML не задан `schema:`, dbt по факту использовал схему `demo_src`.
Это видно в `target/manifest.json`.

Фактические source relation:

1. `dwh_flight.demo_src.aircrafts`
2. `dwh_flight.demo_src.airports`
3. `dwh_flight.demo_src.seats`
4. `dwh_flight.demo_src.bookings`
5. `dwh_flight.demo_src.boarding_passes`
6. `dwh_flight.demo_src.flights`
7. `dwh_flight.demo_src.ticket_flights`
8. `dwh_flight.demo_src.tickets`

### Целевые таблицы моделей

Все 8 SQL-моделей содержат `config(materialized = 'table')`, значит dbt создаёт именно таблицы.

Они строятся в:

`dwh_flight.intermediate`

Итоговые таблицы:

1. `dwh_flight.intermediate.stg_flights__aircrafts`
2. `dwh_flight.intermediate.stg_flights__airports`
3. `dwh_flight.intermediate.stg_flights__seats`
4. `dwh_flight.intermediate.stg_flights__bookings`
5. `dwh_flight.intermediate.stg_flights__boarding_passes`
6. `dwh_flight.intermediate.stg_flights__flights`
7. `dwh_flight.intermediate.stg_flights__ticket_flights`
8. `dwh_flight.intermediate.stg_flights__tickets`

### Где работают тесты

Для тестов dbt использует audit-схему:

`dwh_flight.intermediate_dbt_test__audit`

Именно туда dbt может временно писать служебные relations для тестирования.


## 6. Что делают SQL-модели

Все текущие staging-модели очень простые: каждая читает одну source-таблицу и выбирает нужные поля без `join`.

Соответствие такое:

1. `stg_flights__aircrafts.sql` читает `source('demo_src', 'aircrafts')`
2. `stg_flights__airports.sql` читает `source('demo_src', 'airports')`
3. `stg_flights__seats.sql` читает `source('demo_src', 'seats')`
4. `stg_flights__bookings.sql` читает `source('demo_src', 'bookings')`
5. `stg_flights__boarding_passes.sql` читает `source('demo_src', 'boarding_passes')`
6. `stg_flights__flights.sql` читает `source('demo_src', 'flights')`
7. `stg_flights__ticket_flights.sql` читает `source('demo_src', 'ticket_flights')`
8. `stg_flights__tickets.sql` читает `source('demo_src', 'tickets')`

Так как `ref()` между моделями сейчас нет, зависимости между моделями отсутствуют.
Все модели зависят только от своих source-таблиц.


## 7. Что происходит при выполнении `dbt build` именно в этом проекте

Если запускать команду:

```bash
dbt build
```

то по шагам происходит следующее:

1. dbt читает `dbt_project.yml`
2. определяет имя проекта: `dbt_course_practice`
3. определяет профиль: `dbt_course_practice`
4. идёт в `C:\Users\ilyao\.dbt\profiles.yml`
5. берёт target `dev`
6. открывает подключение к Postgres на `localhost:4001`, база `dwh_flight`
7. подгружает проектные папки `models`, `macros`, `tests`, `seeds`, `snapshots`, `analyses`
8. читает YAML-файлы с source-описаниями и тестами
9. читает SQL-модели
10. компилирует `source('demo_src', '...')` в реальные relation вида `dwh_flight.demo_src.<table>`
11. строит граф зависимостей
12. проверяет, какие схемы уже существуют в БД
13. начинает строить модели в схеме `intermediate`
14. для каждой модели создаёт временную таблицу `__dbt_tmp`
15. затем переименовывает её в финальную таблицу
16. старую версию таблицы, если была, переносит в `__dbt_backup`
17. после успешного переименования удаляет backup-таблицу
18. после построения ресурсов запускает тесты
19. пишет артефакты в папку `target/`
20. пишет подробный лог в `logs/dbt.log`

По логам успешного запуска у вас dbt завершал так:

1. `8 table models`
2. `2 data tests`
3. всего `10` шагов


## 8. В каком порядке строятся модели

Так как между моделями нет `ref()`, строгой последовательности между ними нет.
dbt может выполнять их параллельно, потому что каждая модель независима.

Фактически ограничение задаёт только `threads: 4`.

В последнем успешном запуске были выполнены:

1. `stg_flights__airports`
2. `stg_flights__seats`
3. `stg_flights__flights`
4. `stg_flights__bookings`
5. source test `not_null` для `aircrafts.aircraft_code`
6. source test `unique` для `aircrafts.aircraft_code`
7. `stg_flights__aircrafts`
8. `stg_flights__tickets`
9. `stg_flights__boarding_passes`
10. `stg_flights__ticket_flights`

Но важно понимать:
это не обязательный логический порядок проекта, а порядок одного из запусков.
Из-за параллельности он может немного меняться.


## 9. Роль конкретных файлов

### `dbt_project.yml`
Главный конфиг проекта.
Здесь у вас задаются:

1. имя проекта
2. версия проекта
3. профиль `dbt_course_practice`
4. пути к папкам `models`, `tests`, `macros`, `seeds` и т.д.
5. `clean-targets`
6. старый пример конфигурации `models.dbt_course_practice.example.+materialized: view`

Последний пункт сейчас не используется.
Это подтверждается предупреждением из лога:
`models.dbt_course_practice.example` не применяется ни к одному ресурсу.

### `profiles.yml`
Не хранится в проекте, живёт отдельно в `C:\Users\ilyao\.dbt\profiles.yml`.
Он нужен для подключения к БД.

Здесь задаются:

1. тип адаптера
2. хост
3. порт
4. пользователь
5. база данных
6. схема по умолчанию
7. target
8. threads

### `*_source.yml`
Файлы:

1. `_flight__source.yml`
2. `_fligths__facts__sources.yml`

Они описывают:

1. source `demo_src`
2. список исходных таблиц
3. описания колонок
4. тесты
5. freshness для части таблиц

### `*.sql` в `models/staging/flights/`
Описывают преобразования.
Сейчас это staging-слой: каждая модель забирает столбцы из одного source и материализуется в таблицу.

### `_flights__docs.md`
Содержит markdown-блоки документации для dbt docs.


## 10. Freshness и тесты в вашем проекте

В проекте сейчас описаны:

### Тесты

Для `demo_src.aircrafts.aircraft_code`:

1. `not_null`
2. `unique`

Эти тесты попадают в `dbt build` и реально выполняются.

### Freshness

Описан для:

1. `demo_src.bookings` по полю `book_date::timestamp`
2. `demo_src.flights` по полю `actual_departure`

Важно:
наличие freshness в source YAML не означает, что он всегда автоматически проверяется как часть именно вашего запуска.
Для явной проверки обычно используют `dbt source freshness`.


## 11. Что показывает лог по текущему состоянию

Судя по `logs/dbt.log`, раньше у вас был успешный запуск `dbt build`.

Но в последних запусках на `2026-04-20` команда падала уже на этапе подключения к БД:

1. попытка открыть соединение к `localhost:4001`
2. ошибка `Connection refused` / `Permission denied`
3. build останавливается до начала построения моделей

То есть логика проекта корректно читается, но текущая проблема не в моделях, а в доступности Postgres на этом порту.


## 12. Короткий итог по проекту

Ваш проект сейчас устроен так:

1. source-слой читает 8 сырых таблиц из `dwh_flight.demo_src`
2. staging-слой создаёт 8 таблиц в `dwh_flight.intermediate`
3. каждая staging-модель напрямую читает один source
4. между моделями нет зависимостей через `ref()`
5. `dbt build` у вас строит модели и запускает 2 source-теста
6. подключение определяется через `dbt_project.yml` -> `profiles.yml`
7. документация и граф зависимостей сохраняются в `target/`


## 13. Важное замечание

В `_flights__docs.md` у вас есть пример с запросом к `demo.bookings.aircrafts`, но фактический `manifest.json` для текущего проекта показывает source relation:

`dwh_flight.demo_src.aircrafts`

То есть документационный пример сейчас не совпадает с фактической конфигурацией проекта.
