import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from pandas import DataFrame

# Настройки
FIRST_POST = 1
channel = "nodatanogrowth" # y_borzilo
last_post_number = 716  # Укажи актуальное число последнего поста
base_url = f"https://t.me/{channel}/"
profile_texts = ["Пишу про аналитику", "Если у вас есть Telegram", "О карьерном росте"]  # Тексты из шапки

def get_post_preview(post_number):
    url = f"{base_url}{post_number}"
    response = requests.get(url)

    # Проверка доступности поста
    if response.status_code != 200 or "If you have Telegram" in response.text:
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    post_text = soup.find("meta", {"property": "og:description"})
    
    if post_text and post_text.get("content"):
        preview = post_text["content"][:35].replace('\n',' ').strip()  # Берем первые n символов
        
        # Проверяем, не ведет ли ссылка на шапку профиля
        if any(profile_text in preview for profile_text in profile_texts):
            return None
        
        return f"{post_number};{url};{preview}"
    
    return None

# Основной цикл по номерам постов
results = []
for post_number in tqdm(range(FIRST_POST, last_post_number + 1), desc="Обработка постов", leave=True):
    post_info = get_post_preview(post_number)
    if post_info:
        results.append(post_info)
        # print(*post_info.split(';'))  # Выводим сразу, чтобы видеть процесс
        

# Сохранение в файл (если нужно)
# with open("telegram_posts_filtered.txt", "w", encoding="utf-8") as f:
    # f.write("\n".join(results))

DataFrame([row.split(';') for row in results]).to_excel(channel+'.xlsx', index=False)