from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# In-memory storage for todos
todos = []

# HTML template
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Flask To-Do App</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        input[type=text] { padding: 5px; width: 250px; }
        input[type=submit] { padding: 5px 10px; }
        ul { list-style-type: none; padding-left: 0; }
        li { margin: 8px 0; }
        a { color: red; text-decoration: none; margin-left: 10px; }
    </style>
</head>
<body>
<h1>My To-Do List</h1>

<form action="/add" method="post">
    <input type="text" name="todo" placeholder="Enter a new todo" required>
    <input type="submit" value="Add">
</form>

<ul>
{% for idx, todo in enumerate(todos) %}
    <li>{{ todo }} 
        <a href="/delete/{{ idx }}">[Delete]</a>
    </li>
{% endfor %}
</ul>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, todos=todos)

@app.route("/add", methods=["POST"])
def add_todo():
    todo = request.form.get("todo")
    if todo and todo.strip():  # avoid adding empty todos
        todos.append(todo.strip())
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
    return redirect(url_for("home"))

if __name__ == "__main__":
    # Use host 0.0.0.0 for deployment on Render
    app.run(host="0.0.0.0", port=5000, debug=True)
