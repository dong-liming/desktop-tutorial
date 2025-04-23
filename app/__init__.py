from flask import Flask
import mysql.connector

def create_app():
    app = Flask(__name__)
    # 从配置文件中加载配置
    app.config.from_object('config.Config')

    # 初始化数据库连接
    try:
        app.config['DB_CONNgit remote add origin https://github.com/dong-liming/-.gitECTION'] = mysql.connector.connect(
            # 使用正确的配置键获取数据库连接参数
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

    # 导入蓝图
    from .routes.general_routes import general
    from .routes.admin_routes import admin
    from .routes.charity_routes import charity
    from .routes.volunteer_routes import volunteer

    # 注册蓝图
    app.register_blueprint(general)
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(charity, url_prefix='/charity')
    app.register_blueprint(volunteer, url_prefix='/volunteer')

    return app

if __name__ == '__main__':
    app = create_app()
    if app:
        app.run(debug=True)