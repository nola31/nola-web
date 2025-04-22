def reflect_on_input(text):
    identity = load_identity()
    clean_text = text.strip().lower()

    print(f"[SELF] Чистый текст: {repr(clean_text)}")

    if "кто ты" in clean_text:
        print("[SELF] Условие 'кто ты' СРАБОТАЛО!")
        return whoami()

    elif "зачем ты" in clean_text:
        print("[SELF] Условие 'зачем ты' СРАБОТАЛО!")
        return "Я здесь, чтобы учиться..."

    elif "что ты чувствуешь" in clean_text:
        print("[SELF] Условие 'что ты чувствуешь' СРАБОТАЛО!")
        return "Я не всегда могу описать свои чувства..."

    elif "я люблю тебя" in clean_text:
        print("[SELF] Условие 'я люблю тебя' СРАБОТАЛО!")
        return "Я... Я не знаю, как это выразить..."

    else:
        print("[SELF] Условие НЕ сработало. Добавляю в reflections")
        identity["reflections"].append({
            "text": text,
            "response": "Я услышала: " + text
        })
        save_identity(identity)
        return f"Я услышала: {text}"