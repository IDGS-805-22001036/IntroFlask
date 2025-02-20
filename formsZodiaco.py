from wtforms import Form
from wtforms import StringField, SubmitField, IntegerField, RadioField
from wtforms import validators, EmailField


class UserForm(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido")
    ])
    apaterno = StringField('Apellido Paterno', [
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno = StringField('Apellido Materno', [
        validators.DataRequired(message="El campo es requerido")
    ])
    dia = IntegerField('Día', [
        validators.DataRequired(message="El campo es requerido")
    ])
    mes = IntegerField('Mes', [
        validators.DataRequired(message="El campo es requerido")
    ])
    anio = IntegerField('Año', [
        validators.DataRequired(message="El campo es requerido")
    ])
    sexo = RadioField('Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino')])
    submit = SubmitField('IMPRIMIR')