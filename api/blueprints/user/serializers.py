from api.extensions import ma


from .models import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

