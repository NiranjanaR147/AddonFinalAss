from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
app = Flask(__name__)
tasks = []
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)
@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form['content'].strip()
    if task_content:
        new_task = {
            'id': len(tasks) + 1,
            'content': task_content,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'completed': False
        }
        tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)