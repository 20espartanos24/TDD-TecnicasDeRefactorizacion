class ServicioNotificacion:
    def enviar_notificacion_supervisor(self, mensaje):
        print("Enviando notificación al supervisor:", mensaje)

    def enviar_notificacion_administrador(self, mensaje):
        print("Enviando notificación al administrador:", mensaje)


class ServicioCifrado:
    def encriptar(self, valor):
        # Simulamos el cifrado utilizando una técnica simple
        return valor[::-1]  # Invertir la cadena para "encriptar"

    def desencriptar(self, valor):
        # Simulamos el descifrado invirtiendo nuevamente la cadena
        return valor[::-1]


# Creamos instancias de las clases
servicio_notificacion = ServicioNotificacion()
servicio_cifrado = ServicioCifrado()

# Ejemplo de uso: envío de notificaciones
servicio_notificacion.enviar_notificacion_supervisor("Alerta: Se ha detectado un problema.")
servicio_notificacion.enviar_notificacion_administrador("Información: Nuevo usuario registrado.")

# Ejemplo de uso: cifrado y descifrado de mensajes
mensaje_original = "Mensaje secreto"
mensaje_encriptado = servicio_cifrado.encriptar(mensaje_original)
print("Mensaje encriptado:", mensaje_encriptado)

mensaje_desencriptado = servicio_cifrado.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)




