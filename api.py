from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from models import Note
from resources import *

app = Flask(__name__)
api = Api(app)

#Setup the api resource 

api.add_resource(NoteListResource, '/note/', endpoint = 'note')
api.add_resource(NoteResource, '/note/<string:id>', endpoint = 'note')


if __name__ == '__main__':
    app.run(deubg = True)