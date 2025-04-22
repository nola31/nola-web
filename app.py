from flask import Flask, render_template, request
import json
from nola_filter import apply_filter
from nola_self import self_bp, reflect_on_input

app = Flask(__name__)
app.register_blueprint(self_bp)

# Загрузка памяти из файла
def load_memory():
    try:
        with open("memory.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"messages": []}

# Сохранение памяти
def save_memory(memory):
    with open("memory.json", "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    memory = load_memory()
    response = ""

    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        filtered_input = apply_filter(user_input)

        # Добавляем в память
        memory["messages"].append({"from": "user", "text": filtered_input})
        save_memory(memory)

        # Ответ через самопонимание Нолы
        response = reflect_on_input(filtered_input)

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)