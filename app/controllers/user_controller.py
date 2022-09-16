from flask import render_template, redirect, url_for, request, abort
from app.services import user_service

from app.models.user import User

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def index():
    return str(user_service.get_all_users())

def save():
    pass

def show(userId):
    pass

def update(userId):
    pass

def delete(userId):
    pass
