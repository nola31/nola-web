# nola_filter.py

def apply_filter(text):
    """
    Простейший фильтр для архитектурной дисциплины.
    Пока — только очищает пробелы и запрещённые символы.
    Будет расширен под контекстные условия.
    """
    filtered = text.strip()

    # Пример базового фильтра — можно расширять
    blocked_words = ["rtgfthh", "fggh", "ytytfhhh"]
    for word in blocked_words:
        if word in filtered.lower():
            filtered = filtered.replace(word, "[запрещено]")

    return filtered