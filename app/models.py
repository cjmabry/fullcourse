import app
from app import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), unique = True)
    link = db.Column(db.String(255))
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    # provider many to one relationship
    # topic many to one relationship

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<User %r>' % self.name

class Provider(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), unique = True)
    link = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<Category %r>' % self.name

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), unique = True)
    link = db.Column(db.String(255))
    description = db.Column(db.String(255))
    # degree field(s?)

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<Category %r>' % self.name

class Field(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), unique = True)
    link = db.Column(db.String(255))
    description = db.Column(db.String(255))
    # topics

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<Category %r>' % self.name

field_topics = db.Table('field_topics',
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.id')),
    db.Column('field_id', db.Integer, db.ForeignKey('field.id'))
)
