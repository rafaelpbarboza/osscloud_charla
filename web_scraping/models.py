from app import db


class BaseData(object):

    def save(self):
        db.session.add(self)
        db.session.commit()


class ScrapingData(db.Model, BaseData):

    def __init__(self, name, data):
        self.name = name
        self.data = data

    __tablename__ = 'blog_user'
    serialize_only = ('id', 'data', 'role_type', 'users.id')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    data = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'