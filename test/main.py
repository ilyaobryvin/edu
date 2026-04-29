from yaml import load, FullLoader

try:
    # Открываем файл в контекстном менеджере
    with open(file='./employees.yaml', mode='r', encoding='utf-8') as file:
        # Чтение YAML
        result = load(stream=file, Loader=FullLoader)
        # Вывод результата
        print(result)
except Exception as e:
    print(f"[ERROR]: {e}")