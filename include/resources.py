from model import Notes 
from db import session
from datetime import datetime 
from flask.ext.restful import reqparse
from flask.ext.restful import abort
from flask.ext.restful import Resource
from flask.ext.restful import fields
from flask.ext.restful import marshal_with




#Here we parse so we can use it as objects
parser = reqparser.RequestParser()
parser.add_argument('title')
parser.add_argument('description')
parser.add_argument('create_at')
parser.add_argument('create_by')
parser.add_argument('priority')


class NoteResource(Resource):
    @marshal_with(note_fields) #decorator that takes data objects from API and applies field filtering
    def get(self, id):
        note = session.query(Note).filter(Note.id == id).first()
        
        if not note:
            abort(404, message = 'Note {} doesnt exist'.format(id))
        return note
    def delete(self, id):
        note = session.query(Note).filter(Note.id == id).first()
        
        if not note: 
            abort(404, message = "Note {} doesnt exist".format(id))
            #here we delete de note that has de id passed as argument
        session.delete(note)
        session.commit()
        return {}, 204
    
    @marshal_with(note_fields)
    def put(self, id):
        parsed_args = parser.parsed_args()
        note = session.query(Note).filter(Note.id == id).first()
        note.title = parsed_args['title']
        note.description = parsed_args['description']
        note.create_at = parsed_args['create_at']
        note.create_by = parsed_args['create_by']
        note.priority = parsed_args['pririoty']
        return note, 201
        
class NoteListResource(Resource):
    @marshal_with(note_fields)
    def post(self, id):
        parsed_args = parser.parsed_args()
        note = Note(title = parsed_args['title'], 
                    description = parsed_args['description'],
                    create_at = parsed_args['create_at'],
                    create_by = parsed_args['create_by'],
                    priority = parsed_args['priority'])
        
        session.add(note)
        session.commit()
        return note, 201
    
        
