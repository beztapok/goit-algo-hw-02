from collections import deque

def is_palindrome(s):
    # Приведення рядка до нижнього регістру та видалення пробілів
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Створення двосторонньої черги
    char_deque = deque(s)
    
    # Порівняння символів з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Приклади використання
test_strings = [
    "A man a plan a canal Panama",
    "racecar",
    "hello",
    "Was it a car or a cat I saw",
    "No lemon no melon"
]

for test in test_strings:
    result = "є паліндромом" if is_palindrome(test) else "не є паліндромом"
    print(f"Рядок '{test}' {result}.")
