from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# In-memory storage for todos
todos = []

# HTML template for the To-Do list
HTML_TEMPLATE = """
<!doctype html>
<title>Simple To-Do List</title>
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
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, todos=todos)

@app.route("/add", methods=["POST"])
def add_todo():
    todo = request.form.get("todo")
    if todo:
        todos.append(todo)
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
