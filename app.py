from flask import Flask, render_template
from nonexistent_module import something  # This will cause an import error

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to Flask App</h1><a href="/about">About</a>'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
