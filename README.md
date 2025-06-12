# 📝 To-Do Flask App

A simple and user-friendly **To-Do List Web Application** built using **Python Flask**, allowing users to manage tasks with due dates, categories, completion status, and more.

##  Features

-  Add new tasks with title, due date, and category
-  Categorize tasks (Work, Personal, Study, etc.)
-  Mark tasks as completed or pending
-  Search tasks by keyword
-  Delete or edit tasks easily
-  Toggle light/dark mode UI
-  Highlight overdue tasks in red
-  Mobile responsive design


##  Tech Stack

- **Python** (Flask)
- **HTML5/CSS3**
- **JavaScript** (for dark mode toggle)
- **Jinja2 Templating**
- **JSON** (for storing tasks)

##  Project Structure


```
todo_flask_app/
│
├── app.py             # Main Flask application
├── tasks.json         # JSON file to store to-do tasks
│
├── templates/         # HTML templates
│   └── index.html     # Main UI of the app
│
├── static/            # Static files like CSS
│   └── style.css      # Custom styling
│
└── README.md          # Project overview and instructions
```


##  Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HarithaRavichandar/todo-flask-app.git
   cd todo-flask-app
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open your browser and go to:
   http://127.0.0.1:5000
   


