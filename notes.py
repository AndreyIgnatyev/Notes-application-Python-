import json
import os
from datetime import datetime

# Функция загрузки заметок из файла
def load_notes():
    if os.path.exists('notes.json'):
        try:
            with open('notes.json', 'r', encoding='utf-8') as file:
                data = file.read()
                if data.strip():  # Проверяем, не пустой ли файл
                    return json.loads(data)
                else:
                    return []  # Возвращаем пустой список, если файл пуст
        except json.JSONDecodeError:
            return []  # Возвращаем пустой список, если файл поврежден
    return []  # Возвращаем пустой список, если файл не существует
