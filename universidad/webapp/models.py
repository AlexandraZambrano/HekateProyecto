from django.db import models

# Create your models here.
class Curso(models.Model):
    id_curso = models.CharField(max_length=50, null=False)
    nom_curso = models.CharField(max_length=50, null=False)
    nivel = models.CharField(max_length=1, null=False)

    def __str__(self):
        return f'Curso {self.id}: {self.id_curso} {self.nom_curso} {self.nivel}'



class Estudiante(models.Model):
    id_Estudiante = models.CharField(max_length=50, null=False)
    apellido_1 = models.CharField(max_length=100, null=False)
    apellido_2 = models.CharField(max_length=100, null=False)
    nombre = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'Estudiante {self.id}: {self.nombre} {self.apellido_1}'

    # REVISAR lo de la primaryKey  *otras propiedades*
     #category = models.ForeignKey(Curso, related_name="Estudiante", blank=True, null=True,

class Profesor(models.Model):
    id_Profesor = models.CharField(max_length=50, null=False)
    apellido_1 = models.CharField(max_length=100, null=False)
    apellido_2 = models.CharField(max_length=100, null=False)
    nombre = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)

class Asignatura(models.Model):
    id_Asignatura = models.CharField(max_length=50, null=False)
    # CONECTAR CON foreignKey --> profesor
    nombre_asignatura =models.CharField(max_length=100, null=False)

class Calificaciones(models.Model):
    id_Estudiante = models.CharField(max_length=100, null=False)
    id_Asignatura = models.CharField(max_length=100, null=False)
    puntuacion = models.FloatField(max_length=100, null=False)

class EstudianteProfesor(models.Model):
    Profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)
    Estudiante = models.ManyToManyField(Estudiante)

class Domicilio(models.Model):
    calle = models.CharField(max_length=100)
    numero_calle = models.IntegerField(max_length=5)






