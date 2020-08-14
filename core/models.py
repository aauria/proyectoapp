from django.db import models

# Create your models here.
class Docente(models.Model):
    nombre = models.CharField(max_length=200,default='')
    apellido = models.CharField(max_length=200,default='')
    edad = models.IntegerField()
    email= models.EmailField(max_length=200,default='')
    sexo= (('F','Femenino'),('M','Masculino'))
    sexo=models.CharField(max_length=1,choices=sexo,default='M')
    estado= models.CharField(max_length=15,default='')
    user_mod=models.CharField(max_length=15,default='')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='tr_docente'
        verbose_name='docente'
        verbose_name_plural='docentes'

    def __str__( self ):
        return '{0} {1}'.format(self.apellido, self.nombre)