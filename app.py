from flask import Flask, render_template, request

app = Flask(__name__)

# Factores de conversión para longitud
LENGTH_CONVERSIONS = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1,
    "kilometer": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34,
}

# Factores de conversión para peso
WEIGHT_CONVERSIONS = {
    "milligram": 0.000001,
    "gram": 0.001,
    "kilogram": 1,
    "ounce": 0.0283495,
    "pound": 0.453592,
}

# Funciones de conversión de temperatura
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/length", methods=["GET", "POST"])
def length():
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        # Convertir a metros primero
        in_meters = value * LENGTH_CONVERSIONS[from_unit]
        # Convertir de metros a la unidad deseada
        result = in_meters / LENGTH_CONVERSIONS[to_unit]

        return render_template("length.html", result=result)
    return render_template("length.html")

@app.route("/weight", methods=["GET", "POST"])
def weight():
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        # Convertir a kilogramos primero
        in_kilograms = value * WEIGHT_CONVERSIONS[from_unit]
        # Convertir de kilogramos a la unidad deseada
        result = in_kilograms / WEIGHT_CONVERSIONS[to_unit]

        return render_template("weight.html", result=result)
    return render_template("weight.html")

@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = celsius_to_fahrenheit(value)
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = fahrenheit_to_celsius(value)
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = celsius_to_kelvin(value)
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = kelvin_to_celsius(value)
        else:
            result = value  # Si las unidades son iguales

        return render_template("temperature.html", result=result)
    return render_template("temperature.html")

if __name__ == "__main__":
    app.run(debug=True)