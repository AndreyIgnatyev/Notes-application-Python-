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

# Функция чтения одной заметки по ID
def read_note_by_id():
    notes = load_notes()
    try:
        note_id = int(input("Введите ID заметки для просмотра: "))
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        return

    for note in notes:
        if note['id'] == note_id:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Дата: {note['timestamp']}")
            print(f"Тело: {note['body']}")
            return
    print("Заметка с таким ID не найдена.")

# Функция выборки заметок по дате
def filter_notes_by_date():
    notes = load_notes()
    if not notes:
        print("Заметок нет.")
        return

    date_input = input("Введите дату для фильтрации (формат: ГГГГ-ММ-ДД): ")
    try:
        filter_date = datetime.strptime(date_input, "%Y-%m-%d").date()
    except ValueError:
        print("Ошибка: Неверный формат даты. Используйте ГГГГ-ММ-ДД.")
        return

    found_notes = []
    for note in notes:
        note_date = datetime.strptime(note['timestamp'], "%Y-%m-%d %H:%M:%S").date()
        if note_date == filter_date:
            found_notes.append(note)

    if found_notes:
        print(f"Найдены заметки за дату {date_input}:")
        for note in found_notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")
            print(f"Тело: {note['body']}\n")
    else:
        print(f"Заметок за дату {date_input} не найдено.")
        