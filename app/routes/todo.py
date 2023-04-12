from flask_restful import Resource
from flask import request
from ..utils.dbo import db
from ..models.todo import Todo
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..utils.applogger import mylogger
from sqlalchemy import desc
from datetime import datetime

class TodoRoute(Resource):

    @mylogger.catch()
    @jwt_required()
    def get(self):
        todos = db.session.query(Todo).filter_by(userid=get_jwt_identity()).order_by(desc(Todo.todoid)).all()
        data_todos = list(x.json() for x in todos)

        return {"msg":"ok", "data":data_todos}, 200
    
    @mylogger.catch()
    @jwt_required()
    def post(self):

        title = request.form['title']
        desc = request.form['desc']

        new_todo = Todo(title=title, desc=desc, userid=get_jwt_identity())

        db.session.add(new_todo)
        db.session.commit()

        return {"msg":"ok", "data":"new todo item has been created!" }, 201

    @mylogger.catch()
    @jwt_required()
    def put(self):
        todo_id = request.form['todo_id']
        title = request.form['title']
        desc = request.form['desc']
        updated_at = datetime.now()

        todo_to_save = db.session.query(Todo).filter_by(todoid=todo_id).first()

        todo_to_save.title = title
        todo_to_save.desc = desc
        todo_to_save.updated_at = updated_at
        
        db.session.commit()

        return {"msg":"ok", "data":"todo item has been saved!" }, 200

    @mylogger.catch()
    @jwt_required()
    def delete(self):
        todo_id = request.form['todo_id']
        todo_to_delete = db.session.query(Todo).filter_by(todoid=todo_id).first()

        db.session.delete(todo_to_delete)
        db.session.commit()
        
        return {"msg":"ok", "data":"todo item has been deleted!" }, 200

