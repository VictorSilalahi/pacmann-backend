from flask_restful import Resource
from flask import request, jsonify
from ..utils.dbo import db
from ..models.todo import Todo
from flask_jwt_extended import jwt_required
from ..utils.applogger import mylogger

class TodoStatusRoute(Resource):

    @jwt_required()
    def get(self):
        pass

    @jwt_required()
    def post(self):
        pass

    @mylogger.catch()
    @jwt_required()
    def put(self):
        todo_id = request.form['todo_id']
        todo_status_to_save = db.session.query(Todo).filter_by(todoid=todo_id).first()

        todo_status_to_save.status = "done"
       
        db.session.commit()
        
        return {"msg":"ok", "data":"todo status has been changed!", "todo_id": todo_id }, 200

    @jwt_required()
    def delete(self):
        pass

