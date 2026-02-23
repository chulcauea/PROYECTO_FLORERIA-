from flask import Flask

app = Flask(__name__)

# 1. Ruta principal: Nombre de la florería y propósito
@app.route('/')
def home():
    return """
    <h1>🌸 Bienvenido a Florería 'El Amor de Domenica' 🌸</h1>
    <p>Llevamos la frescura de la naturaleza a tu hogar con los mejores arreglos florales.</p>
    <hr>
    <h3>Nuestros Servicios:</h3>
    <ul>
        <li>Ramos para toda ocasión</li>
        <li>Decoración de eventos</li>
        <li>Entrega a domicilio</li>
    </ul>
    <p>Prueba buscar un ramo en la URL: agrega <b>/flor/Rosas</b> al final del link.</p>
    """

# 2. Ruta dinámica: Consulta de flores/ramos
# Ejemplo: http://127.0.0.1:5000/flor/Girasoles
@app.route('/flor/<tipo>')
def buscar_flor(tipo):
    return f"""
    <h2>Detalle del Producto: {tipo}</h2>
    <p>El ramo de <strong>{tipo}</strong> está disponible para entrega inmediata.</p>
    <p>✨ <i>Precio especial por temporada.</i> ✨</p>
    <br>
    <a href='/'>Volver al inicio</a>
    """

if __name__ == '__main__':
    app.run(debug=True)