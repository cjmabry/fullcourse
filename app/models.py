import app
from app import db

#TO-DO: test course_topics
#TO-DO: define functions to add topics to courses and majors, etc
#TO-DO: get majors from topics, and courses from topics

course_topics = db.Table('course_topics',
    db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'))
)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), unique = True)
    link = db.Column(db.String(255))
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'))
    # topic many to many relationship
    # topics = db.relationship('Topic',
    #     secondary=course_topics,
    #     backref=db.backref('topics',lazy='dynamic'),
    #     lazy='dynamic')

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<Course %r>' % self.name

class Provider(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), unique = True)
    link = db.Column(db.String(255))
    description = db.Column(db.String(255))
    courses = db.relationship('Course', backref='provider',lazy='dynamic')

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<Provider %r>' % self.name

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), unique = True)
    link = db.Column(db.String(255))
    description = db.Column(db.String(255))
    # degree major(s?) many to many

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<Topic %r>' % self.name

major_topics = db.Table('major_topics',
    db.Column('major_id', db.Integer, db.ForeignKey('major.id')),
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'))
)

class Major(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), unique = True)
    link = db.Column(db.String(255))
    description = db.Column(db.String(255))
    topics = db.relationship('Topic',
        secondary=major_topics,
        backref=db.backref('topics',lazy='dynamic'),
        lazy='dynamic')
    parent_id = db.Column(db.Integer, db.ForeignKey('major.id'))
    parent = db.relationship('Major', backref='parent_course',remote_side=id)
    # children one to many

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<Major %r>' % self.name
