from flask import Flask, render_template, request

import forms

app=Flask(__name__)

@app.route("/")
def index():
    titulo="IDGS801"
    lista=["Pedro", "Juan", "Mario"]
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/alumnos",methods=["GET", "POST"])
def alumnos():
    mat=''
    nom=''
    ape=''
    email=''
    alumno_clase=forms.UserFrom(request.form)
    if request.method=="POST":
        mat=alumno_clase.matricula.data
        ape=alumno_clase.apellido.data
        nom=alumno_clase.nombre.data
        email=alumno_clase.email.data
        print('Nombre: {}'.format(nom))
    return render_template("alumnos.html",form=alumno_clase)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/Hola")
def hola():
    return "Hola Mundo!!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola, {user}!"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El numero es: {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"El usuario es: {username} con id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"La suma es: {n1+n2}"

@app.route("/default/")
@app.route("/default/<string:tem>")
def func1(tem='Juan'):
    return f"Hola, {tem}!"

@app.route("/form1/")
def form1():
    return '''
            <form>
            <label for="nombre">Nombre:</lable>
            <input type="text" id="nombre" name="nombre"> </input>
            </form>

            '''

@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def result():
    resultado = ""
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")

        # Convertir los números a enteros
        num1 = int(num1)
        num2 = int(num2)

        if request.form.get("suma") is not None:
            resultado = num1 + num2
            resultado = "La Suma de {} + {} = {}".format(num1, num2, resultado)
        
        elif request.form.get("resta") is not None:
            resultado = num1 - num2
            resultado = "La Resta de {} - {} = {}".format(num1, num2, resultado)
        
        elif request.form.get("multi") is not None:
            resultado = num1 * num2
            resultado = "La multiplicación de {} x {} = {}".format(num1, num2, resultado)
        
        elif request.form.get("div") is not None:
            if num2 != 0: 
                resultado = num1 / num2
                resultado = "La División de {} / {} = {}".format(num1, num2, resultado)
            else:
                resultado = "Error: No se puede dividir por cero."

    return render_template("OperasBas.html", resultado=resultado)



class Total:
    precio_boleto = 12

    def calcular_descuento(self, total, cant_boletos):
        if cant_boletos > 5:
            return total * 0.85  # 15% de descuento
        elif 3 <= cant_boletos <= 5:
            return total * 0.90  # 10% de descuento
        return total  # Sin descuento

    def pago_tarjeta(self, total, forma_pago):
        if forma_pago == "si":
            return total * 0.90  # Descuento adicional del 10%
        return total

@app.route("/Cinepolis")
def Cinepolis():
    return render_template("Cinepolis.html", total="")

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        nombre = request.form.get('nombre', '').strip()
        cant_compradores = request.form.get('cantCompradores', '0').strip()
        cant_boletos = request.form.get('cantBoletos', '0').strip()
        tarjeta_cineco = request.form.get('tarjetaCineco', 'no')

        # Validar que los campos numéricos sean valores enteros válidos
        if not cant_compradores.isdigit() or not cant_boletos.isdigit():
            return render_template('Cinepolis.html', total="Error: Ingresa valores numéricos válidos")

        cant_compradores = int(cant_compradores)
        cant_boletos = int(cant_boletos)

        t = Total()
        total_sin_descuento = cant_boletos * t.precio_boleto
        total_con_descuento = t.calcular_descuento(total_sin_descuento, cant_boletos)
        total_final = t.pago_tarjeta(total_con_descuento, tarjeta_cineco)

        return render_template('Cinepolis.html', total=round(total_final, 2))

    except Exception as e:
        return render_template('Cinepolis.html', total=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True, port=3000)