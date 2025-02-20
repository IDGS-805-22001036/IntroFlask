from wtforms import Form
#from Flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FieldList,RadioField,IntegerField,EmailField
from wtforms import validators, EmailField

class UserFrom(Form):
    matricula=StringField('Matricula',[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="El campo debe tener entre 3 y 10 caracteres")
    ])
    nombre=StringField('Nombre',[
        validators.DataRequired(message="El campo es requerido"),
    ])

    apellido=StringField('Apellido',[
        validators.DataRequired(message="El campo es requerido"),
    ])
    email=StringField('Email',[
        validators.Email(message="Ingrese un correo valido")])