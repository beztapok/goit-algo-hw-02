import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()

def generate_request():
    # Створити нову заявку (наприклад, унікальний номер)
    new_request = random.randint(1, 1000)
    print(f"Нова заявка створена: {new_request}")
    # Додати заявку до черги
    request_queue.put(new_request)

def process_request():
    # Якщо черга не пуста
    if not request_queue.empty():
        # Видалити заявку з черги
        request = request_queue.get()
        # Обробити заявку
        print(f"Обробка заявки: {request}")
    else:
        # Вивести повідомлення, що черга пуста
        print("Черга пуста. Немає заявок для обробки.")

def main():
    try:
        while True:
            # Виконати generate_request() для створення нових заявок
            generate_request()
            # Виконати process_request() для обробки заявок
            process_request()
            # Додати затримку для імітації реального часу обробки
            time.sleep(1)
    except KeyboardInterrupt:
        print("Вихід з програми.")

if __name__ == "__main__":
    main()
