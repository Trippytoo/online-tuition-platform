"""
- Come up with an Idea and  3 to 5 models (account for relationships)
- Create the complete routes for each model (C.R.U.D)
- Create a postman collection of all models for those routes

# Idea: Online Tution Platform

Models & Relationships
User Model ->Students and tutors

Tutor Profile Model -> Tutors' expertise and availability

Lesson Model -> Scheduled learning sessions

Review Model -> Feedback on tutors

Relationships:
A User can be either a tutor or a student.

A User can have one Tutor Profile if they register as a tutor.

A Student can book multiple Lessons.

A Lesson is associated with a Tutor Profile and a Student.

A Review belongs to a Student and references a Tutor Profile.
"""
from flask import Flask
from flask_restful import Api, Resource
from flask_migrate import Migrate

from models import db 
from resources.user import  UserResource
from resources.lesson import LessonResource

#initialize the Flask application
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///online-tuition.db"

app.config["SQLALCHEMY_ECHO"] = True

api = Api(app)

migrate = Migrate(app, db)

db.init_app(app)

# define a route for the root URL
@app.route("/", methods=['GET'])
def index():
    return {"message": "Are you ready to learn?"}

api.add_resource(UserResource, "/users", "/users/<int:user_id>")

api.add_resource(LessonResource, "/lessons", "/lessons/<int:id>")

#C.R.U.D for User Model
#POST /users         → Create a new user (student/tutor)
# @app.post("/users")
# def create_user():
#     return {"message": "User created successfully!"}


# #GET /students         → Fetch all users
# @app.get("/students")
# def get_users():
#     return []

# #GET /students/{id}     → Fetch a specific user
# @app.get("/students/<int:id>")
# def get_user(id):
#     return {"message": f"User with ID {id} fetched successfully!"}

# #PUT /students/{id}     → Update user details
# @app.put("/students/<int:id>")
# def update_user(id):
#     return {"message": f"User with ID {id} updated successfully!"}

# #DELETE /students/{id}  → Delete a user
# @app.delete("/students/<int:id>")
# def delete_user(id):
#     return {"message": f"User with ID {id} deleted successfully!"}


# #C.R.U.D for Tutor Profile Model
# #POST /tutors        → Create a tutor profile
# @app.post("/tutors")
# def create_tutor_profile():
#     return {"message": "Tutor profile created successfully!"}

# #GET /tutors         → Fetch all tutor profiles
# @app.get("/tutors")
# def get_tutor_profiles():
#     return []

# #GET /tutors/{id}    → Fetch a specific tutor
# @app.get("/tutors/<int:id>")
# def get_tutor_profile(id):
#     return {"message": f"Tutor profile with ID {id} fetched successfully!"}

# #PUT /tutors/{id}    → Update tutor profile
# @app.put("/tutors/<int:id>")
# def update_tutor_profile(id):
#     return {"message": f"Tutor profile with ID {id} updated successfully!"}

# #DELETE /tutors/{id} → Delete a tutor profile
# @app.delete("/tutors/<int:id>")
# def delete_tutor_profile(id):
#     return {"message": f"Tutor profile with ID {id} deleted successfully!"}