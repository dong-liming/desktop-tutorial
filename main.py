from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'volunteer_platform'
}

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

# Routes
@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM events WHERE start_date >= CURDATE() LIMIT 5")
    events = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('home.html', events=events)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_type = request.form.get('user_type')  # volunteer, charity, admin

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s AND user_type=%s", (email, password, user_type))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            session['user_id'] = user['id']
            session['user_type'] = user['user_type']
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid login credentials', 401

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['user_type']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password, user_type) VALUES (%s, %s, %s, %s)", 
                       (name, email, password, user_type))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_type = session['user_type']
    
    if user_type == 'volunteer':
        return redirect(url_for('volunteer_dashboard'))
    elif user_type == 'charity':
        return redirect(url_for('charity_dashboard'))
    elif user_type == 'admin':
        return redirect(url_for('admin_dashboard'))

@app.route('/volunteer/dashboard')
def volunteer_dashboard():
    if 'user_id' not in session or session['user_type'] != 'volunteer':
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM events WHERE id IN (SELECT event_id FROM registrations WHERE volunteer_id=%s)", (session['user_id'],))
    events = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('volunteer_dashboard.html', events=events)

@app.route('/charity/dashboard')
def charity_dashboard():
    if 'user_id' not in session or session['user_type'] != 'charity':
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM events WHERE charity_id=%s", (session['user_id'],))
    events = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('charity_dashboard.html', events=events)

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'user_id' not in session or session['user_type'] != 'admin':
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) as volunteer_count FROM users WHERE user_type='volunteer'")
    volunteer_count = cursor.fetchone()['volunteer_count']

    cursor.execute("SELECT COUNT(*) as charity_count FROM users WHERE user_type='charity'")
    charity_count = cursor.fetchone()['charity_count']

    cursor.execute("SELECT COUNT(*) as event_count FROM events")
    event_count = cursor.fetchone()['event_count']

    stats = {
        'volunteer_count': volunteer_count,
        'charity_count': charity_count,
        'event_count': event_count
    }
    cursor.close()
    conn.close()
    return render_template('admin_dashboard.html', stats=stats)

# Add more routes as needed

if __name__ == '__main__':
    app.run(debug=True)