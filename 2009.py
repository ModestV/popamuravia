#!/usr/bin/env python3
"""
Простой CLI менеджер задач (To-Do).
Сохраняет данные в файл todo_data.json в той же папке.
Python 3.7+
"""

import json
import os
from datetime import datetime

DATA_FILE = "todo_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_data(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def new_task(tasks):
    title = input("Название задачи: ").strip()
    if not title:
        print("Пустое название — отменено.")
        return
    notes = input("Дополнительно (опционально): ").strip()
    task = {
        "id": int(datetime.now().timestamp() * 1000),
        "title": title,
        "notes": notes,
        "created": datetime.now().isoformat(timespec='seconds'),
        "done": False,
        "done_at": None
    }
    tasks.append(task)
    save_data(tasks)
    print("Задача добавлена.")

def list_tasks(tasks, show_all=False):
    if not tasks:
        print("Список задач пуст.")
        return
    filtered = tasks if show_all else [t for t in tasks if not t["done"]]
    if not filtered:
        print("Нет задач для отображения (фильтр).")
        return
    print("\n--- Задачи ---")
    for i, t in enumerate(filtered, 1):
        status = "✓" if t["done"] else " "
        print(f"{i}. [{status}] {t['title']} (id: {t['id']})")
        if t.get("notes"):
            print(f"    → {t['notes']}")
        print(f"    создано: {t['created']}" + (f", выполнено: {t['done_at']}" if t["done"] else ""))
    print("---------------\n")

def find_by_id(tasks, id_str):
    try:
        id_val = int(id_str)
    except ValueError:
        return None
    for t in tasks:
        if t["id"] == id_val:
            return t
    return None

def mark_done(tasks):
    id_str = input("Введите id задачи для отметки как выполненной: ").strip()
    t = find_by_id(tasks, id_str)
    if not t:
        print("Задача с таким id не найдена.")
        return
    if t["done"]:
        print("Эта задача уже отмечена как выполненная.")
        return
    t["done"] = True
    t["done_at"] = datetime.now().isoformat(timespec='seconds')
    save_data(tasks)
    print("Задача отмечена как выполненная.")

def delete_task(tasks):
    id_str = input("Введите id задачи для удаления: ").strip()
    t = find_by_id(tasks, id_str)
    if not t:
        print("Задача с таким id не найдена.")
        return
    tasks.remove(t)
    save_data(tasks)
    print("Задача удалена.")

def search_tasks(tasks):
    q = input("Поиск (фраза): ").strip().lower()
    if not q:
        print("Пустой запрос.")
        return
    results = [t for t in tasks if q in t["title"].lower() or q in (t.get("notes") or "").lower()]
    if not results:
        print("Ничего не найдено.")
        return
    print(f"Найдено {len(results)} задач:")
    for t in results:
        status = "✓" if t["done"] else " "
        print(f"- [{status}] {t['title']} (id: {t['id']})")

def show_menu():
    print("""
Выберите действие:
 1 — Показать текущие задачи (невыполненные)
 2 — Показать все задачи
 3 — Добавить задачу
 4 — Отметить задачу как выполненную
 5 — Удалить задачу
 6 — Поиск по задачам
 7 — Сбросить (удалить все задачи)  <-- ОСТОРОЖНО
 0 — Выход
""")

def reset_all(tasks):
    confirm = input("Вы уверены? Введите 'YES' чтобы подтвердить сброс: ").strip()
    if confirm == "YES":
        tasks.clear()
        save_data(tasks)
        print("Все задачи удалены.")
    else:
        print("Отмена.")

def main():
    tasks = load_data()
    while True:
        show_menu()
        choice = input("Ваш выбор: ").strip()
        if choice == "1":
            list_tasks(tasks, show_all=False)
        elif choice == "2":
            list_tasks(tasks, show_all=True)
        elif choice == "3":
            new_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            search_tasks(tasks)
        elif choice == "7":
            reset_all(tasks)
        elif choice == "0":
            print("Пока! Данные сохранены.")
            break
        else:
            print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
