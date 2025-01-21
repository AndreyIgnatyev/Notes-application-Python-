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

# Функция сохранения заметок в файл
def save_notes(notes):
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)

# Функция добавления новой заметки
def add_note():
    notes = load_notes()
    note_id = notes[-1]['id'] + 1 if notes else 1 
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        'id': note_id,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена.")

# Функция чтения всех заметок
def read_notes():
    notes = load_notes()
    if not notes:
        print("Заметок нет.")
        return
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")
        print(f"Тело: {note['body']}\n")