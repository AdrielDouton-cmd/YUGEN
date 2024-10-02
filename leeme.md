# YUGEN

# Esta pagina pertenece a un local gastronomico ficticio 

*Pasos de testeo*

1. Entrar a la pagina principal 'http://127.0.0.1:8000/web-yugen/'
'''
Aca se lanza la view 'inicio' que renderiza el archivo 'inicio.html' el cual hereda de 'padre.html'
'''

2. Registrar cliente
'''
Entrar a la pagina 'http://127.0.0.1:8000/web-yugen/registrarse/' que permite el registro de clientes:
Se lanza la view 'crear_registro' que toma el modelo Cliente para usarlo en un formulario y renderiza el archivo 'registrarse.html' que permite cargar datos de cliente a la BD
'''

3. Registrar evento
'''
Entrar a la pagina 'http://127.0.0.1:8000/web-yugen/eventos/' que permite crear eventos:
Lanza la view 'crear_evento' que toma el modelo Evento, crea un formulario y renderiza 'eventos.html'
'''

4. Registrar reserva
'''
Entrar a la pagina 'http://127.0.0.1:8000/web-yugen/reserva/' que permite registrar una reserva:
Lanza la view 'crear_reserva' que toma el modelo Reserva, crea un formulario y renderiza 'reserva.html'
'''

5. ADMIN
'''
El funcionaminto de la base de datos se puede corroborar desde la url admin.
user: adriel
password: 1234
'''