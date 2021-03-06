#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from flask_sqlalchemy import SQLAlchemy
from main import app


db = SQLAlchemy(app)


posts_tags = db.Table(
    'posts_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)


class User(db.Model):
    """ Represents Proected Users."""


    # Set the name for table
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(255))
    # Establish contact with Post's ForeignKey: user_id
    posts = db.relationship(
        'Post',
        backref='users',
        lazy='dynamic')


    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    
    def __repr__(self):
        """ Define the string format for instance of User."""
        return "<Model User '{}'>".format(self.username)


class Post(db.Model):
    """Represents Proected posts. """


    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=True)
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    #Set the foreign key for POst
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    # Establish contact with Comments ForeignKey: post_id
    comments = db.relationship(
        'Comment',
        backref='posts',
        lazy='dynamic')
    # many to many: oists <===> tags
    tags = db.relationship(
        'Tag',
        secondary=posts_tags,
        backref=db.backref('posts',
        lazy='dynamic'))


    def __init__(self, title):
        self.title = title


    def __repr__(self):
        return "<Model Post '{}'>".format(self.title)



class Comment(db.Model):
    """ Represents Proected comments. """


    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text)
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))


    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return "<Model Comment '{}'>".format(self.name)


class Tag(db.Model):
    """ Represents Proected tags."""


    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    
    
    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return "<Model Tag '{}'>".format(self.name)