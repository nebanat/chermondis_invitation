from flask import jsonify
from flask_restplus import Resource
from .serializers import UserSchema


class User(Resource):
    def get(self):
        """

        :return:
        """
        user_details = {
            "id": 1,
            "username": "aaron ",
            "email": "abiliyok@gmail.com",
            "is_deleted": True,
            "deleted_at": "2014-08-11T05:26:03.869245",
            "updated_at": "2014-08-11T05:26:03.869245",
            "created_at": "2014-08-11T05:26:03.869245",
        }

        result = UserSchema().dump(user_details)

        return jsonify(dict(data=dict(employees=result.data),
                            status='success'))
