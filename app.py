from flask import Flask, render_template, request
import os


app = Flask(__name__)



def digitsSum(inputInt):
    """
    Regresa la suma de los dígitos de un número entero
    """
    total = 0

    for digito in str(abs(inputInt)):
        total += int(digito)

    return total


def isPalindrome(inputStr):
    """
    Verifica si un texto es palíndromo
    """
    texto = inputStr.lower().strip()
    return texto == texto[::-1]


def integerSort(inputArray):
    """
    Ordena una lista sin usar sort() (Bubble Sort)
    """

    resultado = inputArray.copy()
    n = len(resultado)

    for i in range(n):
        for j in range(0, n - i - 1):

            if resultado[j] > resultado[j + 1]:
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]

    return resultado



@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado_suma = ""
    resultado_palindromo = ""
    resultado_orden = ""
    error = ""

    if request.method == "POST":

        # SUMA DE DÍGITOS
        if "numero" in request.form:

            try:
                numero = int(request.form["numero"])
                resultado_suma = digitsSum(numero)

            except:
                error = "❌ Ingresa un número válido"


        # PALÍNDROMO
        if "texto" in request.form:

            texto = request.form["texto"]
            resultado_palindromo = isPalindrome(texto)


        # ORDENAMIENTO
        if "lista" in request.form:

            try:
                lista = request.form["lista"]
                lista = list(map(int, lista.split(",")))

                resultado_orden = integerSort(lista)

            except:
                error = "❌ Formato incorrecto. Usa: 1,2,3"


    return render_template(
        "index.html",
        suma=resultado_suma,
        palindromo=resultado_palindromo,
        orden=resultado_orden,
        error=error
    )




if __name__ == "__main__":

    puerto = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=puerto,
        debug=True
    )
