class ServicioNotificacion:
    def enviar_notificacion_supervisor(self, mensaje):
        print("Enviando notificación al supervisor:", mensaje)

    def enviar_notificacion_administrador(self, mensaje):
        print("Enviando notificación al administrador:", mensaje)

    def _encriptar(self, valor):
        # Simulamos el cifrado utilizando una técnica simple
        return valor[::-1]  # Invertir la cadena para "encriptar"

    def _desencriptar(self, valor):
        # Simulamos el descifrado invirtiendo nuevamente la cadena
        return valor[::-1]


# Creamos una instancia de la clase
servicio_notificacion = ServicioNotificacion()

# Ejemplo de uso: envío de notificaciones
servicio_notificacion.enviar_notificacion_supervisor("Alerta: Se ha detectado un problema.")
servicio_notificacion.enviar_notificacion_administrador("Información: Nuevo usuario registrado.")

# Ejemplo de uso: cifrado y descifrado de un mensaje
mensaje_original = "Mensaje secreto"
mensaje_encriptado = servicio_notificacion._encriptar(mensaje_original)
print("Mensaje encriptado:", mensaje_encriptado)

mensaje_desencriptado = servicio_notificacion._desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)


