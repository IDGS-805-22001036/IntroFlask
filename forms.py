from wtforms import Form
#from Flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FieldList,RadioField,IntegerField

class UserFrom(Form):
    matricula=StringField('Matricula')
    nombre=StringField('Nombre')
    apellido=StringField('Apellido')
    email=StringField('Email')