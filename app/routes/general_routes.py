from flask import Blueprint, render_template, request, redirect, url_for, session
import mysql.connector

general = Blueprint('general', __name__)

# 主页路由
@general.route('/')
def home():
    return render_template('home.html')

# 登录路由
@general.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            # 连接数据库
            db = mysql.connector.connect(
                host='localhost',
                user='root',
                password='dlm200401250012',
                database='volunteer_platform'
            )
            cursor = db.cursor()
            # 查询用户信息
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
            db.close()

            if user:
                # 登录成功，将用户 ID 存入 session
                session['user_id'] = user[0]
                return redirect(url_for('general.home'))
            else:
                # 登录失败，返回错误信息
                error = 'Invalid username or password. Please try again.'
                return render_template('login.html', error=error)

        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            error = 'Database error. Please try again later.'
            return render_template('login.html', error=error)

    return render_template('login.html')

# 注册路由
@general.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user_type = request.form.get('user_type')

        if not username or not email or not password or not user_type:
            error = 'All fields are required. Please try again.'
            return render_template('register.html', error=error)

        try:
            # 连接数据库
            db = mysql.connector.connect(
                host='localhost',
                user='root',
                password='dlm200401250012',
                database='volunteer_platform'
            )
            cursor = db.cursor()
            # 检查用户名是否已存在
            query = "SELECT * FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                error = 'Username already exists. Please choose another one.'
                db.close()
                return render_template('register.html', error=error)

            # 插入用户信息
            query = "INSERT INTO users (username, email, password, user_type) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (username, email, password, user_type))
            db.commit()
            db.close()

            return redirect(url_for('general.login'))

        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            error = 'Registration failed. Please try again.'
            return render_template('register.html', error=error)

    return render_template('register.html')