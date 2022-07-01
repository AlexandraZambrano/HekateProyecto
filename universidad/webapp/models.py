from django.db import models

# Create your models here.
class Curso(models.Model):
    nivel = models.CharField(max_length=1, null=False)

    def __str__(self):
        return f'Curso {self.id}: {self.nivel}'

class Estudiante(models.Model):
    apellido_1 = models.CharField(max_length=100, null=False)
    apellido_2 = models.CharField(max_length=100, null=False)
    nombre = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'Estudiante {self.id}: {self.nombre} {self.apellido_1} {self.curso}'

    # REVISAR lo de la primaryKey  *otras propiedades*
     #category = models.ForeignKey(Curso, related_name="Estudiante", blank=True, null=True,

class Profesor(models.Model):
    apellido_1 = models.CharField(max_length=100, null=False)
    apellido_2 = models.CharField(max_length=100, null=False)
    nombre = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    def __str__(self):
        return f'Profesor {self.id}: {self.nombre} {self.apellido_1}'

class Asignatura(models.Model):
    # CONECTAR CON foreignKey --> profesor
    nombre_asignatura = models.CharField(max_length=100, null=False)
    Profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'Asignatura {self.id}: {self.nombre_asignatura} {self.Profesor}'

class Calificaciones(models.Model):
    Estudiante = models.ManyToManyField(Estudiante)
    Asignatura = models.ManyToManyField(Asignatura)
    puntuacion = models.FloatField(max_length=100, null=False)
    def __str__(self):
        return f'Calificaciones {self.id}: {self.Estudiante} {self.Asignatura}'

class EstudianteProfesor(models.Model):
    Profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)
    Estudiante = models.ManyToManyField(Estudiante)







