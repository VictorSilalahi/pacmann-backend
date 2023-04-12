from flask_restful import Resource
from flask import request
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from ..utils.dbo import db
from ..models.user import User
from datetime import timedelta
from ..utils.applogger import mylogger

class UserRoute(Resource):
    def get(self):
        pass

    @mylogger.catch()
    def post(self):
        email = request.form['email']
        pwd = request.form['password']

        user = db.session.query(User).filter_by(email=email).first()
        if not user:
            return {"msg":"error", "data": "this email is not registered!"}, 401

        if check_password_hash(user.pwd, pwd):
            user_data = {
                "userid": user.userid,
                "username": user.username,
                "email": user.email
            }
            token_range = timedelta(minutes=30)
            token_refresh_range = timedelta(days=30)
            user_token = create_access_token(identity=user.userid, fresh=True, expires_delta=token_range)
            user_refresh_token = create_refresh_token(identity=user.userid, expires_delta=token_refresh_range)
            
            return {"msg":"ok", "token":user_token, "refresh_token":user_refresh_token, "data": user_data}, 200

        else:
            return {"msg":"error", "data": "credential error!"}, 401
    
    def put(self):
        pass

    def delete(self):
        pass
