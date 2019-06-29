from sqlalchemy import Integer, Column, String
from api.extensions import db
from lib.util_sqlalchemy import ResourceMixin


class User(ResourceMixin, db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(24), unique=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False,
                   server_default='')
    password = Column(String(128), nullable=False, server_default='')

    @classmethod
    def find_by_identity(cls, identity):
        """
        Find a user by their e-mail or username.

        :param identity: Email or username
        :type identity: str
        :return: User instance
        """
        return User.query.filter(
            (User.email == identity) | (User.username == identity)).first()




