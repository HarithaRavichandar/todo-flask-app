from flask import Flask, render_template, request, redirect
import json
import os
from datetime import date

app = Flask(__name__)

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE) or os.path.getsize(TASK_FILE) == 0:
        return []
    with open(TASK_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

@app.route("/")
def index():
    tasks = load_tasks()
    search_query = request.args.get('search', '').lower()

    if search_query:
        tasks = [task for task in tasks if search_query in task['title'].lower()]

    current_date = date.today().isoformat()

    indexed_pending = [(i, task) for i, task in enumerate(tasks) if not task["completed"]]
    indexed_completed = [(i, task) for i, task in enumerate(tasks) if task["completed"]]

    progress = int((len(indexed_completed) / len(tasks)) * 100) if tasks else 0

    return render_template("index.html",
                           pending_tasks=indexed_pending,
                           completed_tasks=indexed_completed,
                           progress=progress,
                           search_query=search_query,
                           current_date=current_date)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("task")
    due = request.form.get("due")
    category = request.form.get("category")

    if title:
        tasks = load_tasks()
        tasks.append({
            "title": title,
            "completed": False,
            "due": due if due else "",
            "category": category if category else "General"
        })
        save_tasks(tasks)
    return redirect("/")

@app.route("/complete/<int:task_id>")
def complete(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = not tasks[task_id]["completed"]
        save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
        save_tasks(tasks)
    return redirect("/")

@app.route("/edit/<int:task_id>", methods=["POST"])
def edit(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["title"] = request.form.get("title")
        tasks[task_id]["due"] = request.form.get("due")
        tasks[task_id]["category"] = request.form.get("category")
        save_tasks(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
