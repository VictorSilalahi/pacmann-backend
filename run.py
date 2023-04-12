from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from waitress import serve

from app.utils import dbo

from app.routes.users import UsersRoute
from app.routes.user import UserRoute
from app.routes.todo import TodoRoute
from app.routes.todostatus import TodoStatusRoute

import os
from dotenv import load_dotenv

from flask_jwt_extended import JWTManager

from swagger_gen.swagger import Swagger


m = Migrate()

def create_app():

    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = os.getenv("APP_SECRET_KEY")
    app.config['JWT_SECRET_KEY'] = os.getenv("APP_JWT_SECRET_KEY")

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://"+os.getenv("APP_DB_USERNAME")+":"+os.getenv("APP_DB_PASSWORD")+"@"+os.getenv("APP_DB_HOST")+":"+os.getenv("APP_DB_PORT")+"/"+os.getenv("APP_DB_NAME")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['UPLOAD_FOLDER'] = os.getenv("APP_UPLOAD_FOLDER")

    from app.models.todo import Todo
    from app.models.user import User

    dbo.init_app(app)
    
    m.init_app(app, dbo.db)

    jwt = JWTManager(app)

    api = Api(app)

    api.add_resource(UsersRoute, "/api/users")
    api.add_resource(UserRoute, "/api/user/validate")
    api.add_resource(TodoRoute, "/api/todo")
    api.add_resource(TodoStatusRoute, "/api/todo/status")
    
    swagger = Swagger(app=app, title='API List')
    swagger.configure()
    
    CORS(app)

    return app


if __name__== "__main__":
    
    load_dotenv()

    mode = os.getenv('APP_MODE')
    
    app = create_app()
    
   
    if mode == "dev":
        app.run(host=os.getenv("APP_HOST"), port=os.getenv("APP_PORT"), debug=True)
    else:
        serve(app, host=os.getenv("APP_HOST"), port=os.getenv("APP_PORT"))
    