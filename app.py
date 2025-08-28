from flask import Flask, render_template

app=Flask(__name__)    # Missing spaces around =


@app.route('/')
def home():
    return '<h1>Welcome to Flask App</h1><a href="/about">About</a>'


@app.route('/about') 
def about( ):    # Extra spaces in function definition
    return render_template('about.html')


if __name__=='__main__':    # Missing spaces around ==
    very_long_variable_name_that_exceeds_line_limit = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15
    app.run(debug=True)
