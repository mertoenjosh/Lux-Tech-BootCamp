from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config.from_pyfile('settings.py')

mysql = MySQL(app)


# set database cursor

# set the routes
@app.route('/')
def form():
    return render_template('form.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method != "POST":
        return "Use the sign up form"
    
    if request.method == 'POST':
        details = request.form
        name = details['name']
        email = details['email']
        message = details['message']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users(name, email, message) VALUES (%s, %s, %s)",(name, email, message))
        cursor.connection.commit()
        cursor.close()
        return f'Created user {name}'
