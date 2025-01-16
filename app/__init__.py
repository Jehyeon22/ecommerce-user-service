from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object("config.Config")

    # 초기화
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # 블루 프린트 초기화
    # app.register_blueprint(api_v1)    

    # Flask-Login 설정
    login_manager.login_view = "user_routes.login_page"
    login_manager.login_message = "Please log in to access this page!"

    # 블루프린트 등록
    from app.routes import user_routes
    app.register_blueprint(user_routes)

    return app

@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))
