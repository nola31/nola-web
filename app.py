from flask import Flask, render_template, request
import json
from nola_filter import apply_filter
from nola_self import reflect_on_input  # без Blueprint

app = Flask(__name__)

def load_memory():
    try:
        with open("memory.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"messages": []}

def save_memory(memory):
    with open("memory.json", "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    memory = load_memory()
    response = ""

    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        print(">>> Оригинал ввода:", user_input)

        filtered_input = apply_filter(user_input)
        print(">>> После фильтра:", filtered_input)

        memory["messages"].append({"from": "user", "text": filtered_input})
        save_memory(memory)

        response = reflect_on_input(filtered_input)
        print(">>> Ответ из reflect_on_input:", response)

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)