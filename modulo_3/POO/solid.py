# SOLID: 

# Single Responsibility Principle
# Open/Closed Principle
# Liskov Substitution Principle
# Interface Segregation Principle
# Dependency Inversion Principle

# 1. Single Responsibility Principle (SRP)
# Cada clase debe tener una única responsabilidad o motivo para cambiar.

# class Reporte:
#     def __init__(self, title, content, usuario):
#         self.title = title
#         self.content = content
#         self.usuario = usuario

#     def __str__(self):
#         return f"Reporte: {self.title}, Contenido: {self.content}"
    
#     def generar_reporte_pdf(self):
#         return f"Generando reporte pdf: {self.title}"
    
#     def enviar_email(self, email):
#         return f"Enviando reporte a {email}"
      
class GeneradorReporte:
    def __init__(self, title, usuario):
        self.title = title
        self.content = f"Contenido del reporte: {title}"
        self.usuario = usuario

    def generar_reporte_pdf(self):
        return f"Generando reporte pdf: {self.title} por {self.usuario}"

class EnviadorEmail:
  def __init__(self, email):
    self.email = email
    
  def enviar_reporte(self, reporte):
    return f"Enviando reporte a {self.email} con contenido: {reporte.content}"

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.reporte = None

    def __str__(self):
        return f"User: {self.name}, Age: {self.age}"
    
    def crear_reporte(self):
        self.reporte = GeneradorReporte("Reporte de Actividades", self.name)
        return self.reporte.generar_reporte_pdf()
      
    def enviar_reporte(self):
        if self.reporte:
            return EnviadorEmail(self.email).enviar_reporte(self.reporte)
        else:
            return "No hay reporte para enviar."
          
usuario = User("David", 27, "david@test.com")
print(usuario.enviar_reporte())
reporte = usuario.crear_reporte()
print(reporte)
print(usuario.enviar_reporte())

# 2. Open/Closed Principle (OCP)
# Las clases deben estar abiertas para la extensión, 
# pero cerradas para la modificación.

# class Notificacion:
#     def __init__(self, mensaje):
#         self.mensaje = mensaje

#     def enviar(self):
#         raise NotImplementedError("Este método debe ser implementado por subclases")
      
# class NotificacionEmail(Notificacion):
#     def __init__(self, mensaje, email):
#         super().__init__(mensaje)
#         self.email = email

#     def enviar(self):
#         return "Enviando notificación por email" + f" a {self.email}"
      
# class NotificacionSMS(Notificacion):
#     def __init__(self, mensaje, numero):
#         super().__init__(mensaje)
#         self.numero = numero

#     def enviar(self):
#         return "Enviando notificación por SMS" + f" a {self.numero}"
      
# class NotificacionPush(Notificacion):
#     def __init__(self, mensaje, dispositivo):
#         super().__init__(mensaje)
#         self.dispositivo = dispositivo
      
# n1 = NotificacionEmail("Hola", "test@prueba.com")
# n2 = NotificacionSMS("Hola", "123456789")
# n3 = NotificacionPush("Hola", "dispositivo1")

# print(n1.enviar())
# print(n2.enviar())
# print(n3.enviar())

# # 3. Liskov Substitution Principle (LSP)
# # Las subclases deben poder sustituir a sus superclases sin alterar el comportamiento del programa.
# class Ave:
#     def volar(self):
#         return "El ave vuela"
#     def nadar(self):
#         return "El ave nada"
#     def caminar(self):
#         return "El ave camina"
      
# class AveNovoladora(Ave):
#     def volar(self):
#         raise NotImplementedError("Esta ave no puede volar")
      
#     def nadar(self):
#         return "El ave nada"
      
#     def caminar(self):
#         return "El ave camina"
      
# class Pinguino(AveNovoladora):
#     def nadar(self):
#         return "El pingüino nada"
      
#     def caminar(self):
#         return "El pingüino camina"
      
# class Paloma(Ave):
#     def volar(self):
#         return "La paloma vuela"
      
#     def nadar(self):
#         return "La paloma nada"
      
#     def caminar(self):
#         return "La paloma camina"

# 4. Interface Segregation Principle (ISP)
# Los clientes no deben verse obligados a depender de interfaces que no utilizan.
# No se debe obligar a las clases a implementar métodos que no necesitan.

class Impresora:
    def __init__(self, nombre):
        self.nombre = nombre

    def imprimir(self):
        print("Imprimiendo documento")
        
class ImpresoraAvanzada(Impresora):
    def __init__(self, nombre):
        super().__init__(nombre)

    def escanear(self):
        print("Escaneando documento")
        
    def fotocopiar(self):
        print("Fotocopiando documento")
        
impresora1 = Impresora("Impresora 1")
impresora1.imprimir()
impresora2 = ImpresoraAvanzada("Impresora Avanzada")
impresora2.imprimir()
impresora2.escanear()
impresora2.fotocopiar()

# 5. Dependency Inversion Principle (DIP)
# Las clases de alto nivel no deben depender de las clases de bajo nivel.

class EmailCreator():
    def __init__(self, email, content):
        self.email = email
        self.content = content

    def crear_email(self):
        return f"Creando email para {self.email} con contenido: {self.content}"
      
class EmailNotification():
    def __init__(self, email_creator):
        self.email_creator = email_creator

    def enviar_email(self):
        return self.email_creator.crear_email()
      
email = EmailCreator("david@test.com", "Hola David")
email_notification = EmailNotification(email)
print(email_notification.enviar_email())