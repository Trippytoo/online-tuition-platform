from flask_restful import Resource

from models import Lesson


class LessonResource(Resource):
    def get(self, id=None):
        if id == None:
            lesson = Lesson.query.all()

            return Lesson
        else:
            lesson = Lesson.query.filter_by(id=id).first()
            print(lesson)

            return lesson


    def post(self):
        pass    