from flask_restful import Resource, reqparse
from flask import request
from service import user_service
from . import api

class UserLoginApi(Resource):
    def post(self):
        if not request.is_json:
            return {"msg": "Missing JSON in request"}, 400
            
        data = request.get_json(force=True)
        if not data:
            return {"msg": "Invalid JSON format"}, 400
            
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return {"msg": "Missing username or password"}, 400
        
        
        user = user_service.select_by_username(username)
        
        if not user or user.password != password:
            return {"msg": "username or password error"}, 401
            
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
        
class UserRegisterApi(Resource):
    def post(self):
                    
        data = request.get_json(force=True)
        if not data:
            return {"msg": "Invalid JSON format"}, 400
        
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        
        if not username or not password:
            return {"msg": "Missing username or password"}, 400

        
        try:
            user = user_service.save_user(username, password, email)
            return {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        except ValueError as e:
            return {"msg": str(e)}, 400
        
class UserInfoApi(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True, help='用户ID不能为空', location="args")
        args = parser.parse_args()
        
        user_id = args['user_id']
        
        user = user_service.get_by_user_id(user_id)
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }

api.add_resource(UserLoginApi, "/login")
api.add_resource(UserRegisterApi, "/register")
api.add_resource(UserInfoApi, "/getUser")