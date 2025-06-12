from flask_restful import Resource

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id == None:
            return []
        else:
            return []
        
    def post(self):
        return {"messaage": "User created"}

    def patch(self, user_id):
        return {"message": f"User with ID {user_id} updated successfully!"}

    def delete(self, user_id):
        return {"message": f"User with ID {user_id} deleted successfully!"} 