from flask_restful import Resource
from flask import request
from ..models.user import User
from ..utils.dbo import db
from werkzeug.security import generate_password_hash
from ..utils.applogger import mylogger
from swagger_gen.lib.wrappers import swagger_metadata

class UsersRoute(Resource):

    @mylogger.catch()
    @swagger_metadata(
        request_model={},
        summary='An example route',
        description='This is an example route, check it out!',
        response_model=[(200, 'Success'), (500, 'Error')],
        query_params=[],
        security=''        
    )
    def get(self):
        users = db.session.query(User).all()

        return {"msg":"ok", 'data':list(x.json() for x in users)}, 200

    @mylogger.catch()
    def post(self):
        email = request.form['email']

        user = db.session.query(User).filter_by(email=email).first()
        if user:
            return {"msg":"error", "data": "this email has been registered!"}, 400

        username = request.form['username']
        user_pwd = generate_password_hash(request.form['password1'], method="sha256")

        new_user = User(username=username, email=email, pwd=user_pwd)
        db.session.add(new_user)
        db.session.commit()
        
        return {"msg":"ok", "data":"new user has been created!" }, 201

    def put(self):
        pass

    def delete(self):
        pass
