from telnetlib import SE
from time import sleep
from django.db import models

# Create your models here.



class caratula(models.Model):
    CARATULA = [
    ('Lesiones_leves', 'Lesiones_leves'),
    ('Lesiones_graves', 'Lesiones_graves'),
    ('Amenazas', 'Amenazas'),
    ('Abuso', 'Abuso'),
    ]
    Caratula = models.CharField(max_length= 100, choices = CARATULA )

    def __str__(self):
        return self.Caratula

class Modalidad(models.Model):
    MODALIDAD_VIOLENCIA = [
        ('Domestica', 'Domestica'),
        ('Institucional', 'Institucional'),
        ('Laboral', 'Laboral'),
        ('Reproductiva', 'Reproductiva'),
        ('Mediatica', 'Mediatica'),
        ('Callejera', 'Callejera'),
        ('Obtetrica', 'Obtetrica'),
        ('Fisica', 'Fisica'),
        ('Psicologica', 'Psicologica'),
        ('Simbolica', 'Simbolica'),
        ('Sexual', 'Sexual'),
        ('Economica/patrimonial', 'Economica/patrimonial'),
    ]
    # ej: nombre = models.CharField(max_length=100, unique= True) unique = True se utiliza para que no haya un caracter repetido
    Violencia = models.CharField(max_length= 100, choices = MODALIDAD_VIOLENCIA )    
    
class victima(models.Model):
    dni_victima = models.IntegerField(null=False, blank=False, primary_key= True)

    def dniVictima(self):
         return self.dni_victima

class agresor(models.Model):
    dni_agresor = models.IntegerField(null=False, blank=False, primary_key= True)

    def dniAgresor(self):
         return self.dni_agresor

class niño(models.Model):
    dni_niño = models.IntegerField(null=False, blank=False, primary_key= True)

    def dniNiño(self):
         return self.dni_niño

class casa_de_proteccion(models.Model):
    Casa_de_proteccion = models.CharField(max_length=100, primary_key= True)

    def casaProteccion(self):
        return self.Casa_de_proteccion

class red_de_contencion(models.Model):
    Red_de_contencion = models.CharField(max_length=100, primary_key= True)

    def redContencion(self):
        return self.Red_de_contencion

class informacion(models.Model):
    DNI_victima = models.ForeignKey('victima', on_delete=models.CASCADE)
    DNI_agresor = models.ForeignKey('agresor', on_delete=models.CASCADE)
    DNI_niño = models.ForeignKey('niño', on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=45)
    Apellido = models.CharField(max_length=45)
    Edad = models.IntegerField()
    Fecha_de_nacimiento = models.DateField()
    Trabajo = models.CharField(max_length=45)
    Programa_social = models.CharField(max_length=100)
    Hijos = models.IntegerField()
    Quien_comunica = models.CharField(max_length=100)
    Comentarios = models.CharField(max_length=255)
    Casa_de_proteccion = models.ForeignKey('casa_de_proteccion', on_delete=models.CASCADE)
    Red_de_contencion = models.ForeignKey('red_de_contencion', on_delete=models.CASCADE)

    def __str__(Self):
        txt = "DNI victima: {0} / DNI agresor: {1} / DNI niño {2} / Nombre: {3} / Apellido: {4} / Edad: {5} / Fecha de nacimiento: {6} / Trabajo: {7} / Programa social: {8} / Hijos: {9} / Quien comunica: {10} / Casa de proteccion: {11} / Red de contencion: {12} / Comentarios: {13} "
        return txt.format(Self.DNI_victima.dniVictima(), Self.DNI_agresor.dniAgresor(), Self.DNI_niño.dniNiño(), Self.Nombre, Self.Apellido, Self.Edad, Self.Fecha_de_nacimiento.strftime("%A %d/%m/%Y"), Self.Trabajo, Self.Programa_social, Self.Hijos, Self.Quien_comunica, Self.Casa_de_proteccion.casaProteccion(), Self.Red_de_contencion.redContencion(), Self.Comentarios)
        
class expediente(models.Model):
    Nro_expediente = models.IntegerField(null=False, blank=False, primary_key= True)
    DNI_victima = models.ForeignKey('victima', on_delete=models.CASCADE)
    DNI_agresor = models.ForeignKey('agresor', on_delete=models.CASCADE)
    DNI_niño = models.ForeignKey('niño', on_delete=models.CASCADE)

    def expediente(Self):
        txt = "Nro de expediente: {1} / DNI victima: {1} / DNI agresor: {2} / DNI niño {3}"
        return txt.format(Self.Nro_expediente, Self.DNI_victima.dniVictima(), Self.DNI_agresor.dniAgresor(), Self.DNI_niño.dniNiño()) 

class medida(models.Model):
    Caratula = models.ForeignKey('caratula', on_delete=models.CASCADE)
    Nro_expediente = models.ForeignKey('expediente', on_delete=models.CASCADE)
    DNI_victima = models.ForeignKey('victima', on_delete=models.CASCADE)
    DNI_agresor = models.ForeignKey('agresor', on_delete=models.CASCADE)
    Medida = models.IntegerField()
    Resolucion = models.CharField(max_length=255)
    Alcance = models.CharField(max_length=255)

def __str__(Self):
    txt = "Caratula: {1} / Nro de expediente: {2} / DNI victima: {3} / DNI agresor: {4} / Medida: {5} / Resolucion: {6} / Alcance: {7}"
    return txt.format(Self.Caratula.Caratula(), Self.Nro_expediente.expediente(), Self.DNI_victima.Victima(), Self.DNI_agresor.dniAgresor(), Self.Medida, Self.Resolucion, Self.Alcance)

class periodo(models.Model):
    Año = models.DateField()
    Fecha_recepcion = models.DateField()
    Fecha_medida_plazo = models.DateField()
    Nro_expediente =  models.ForeignKey('expediente', on_delete=models.CASCADE)

def __str__(Self):
    txt = "Año: {1} / Fecha de recepcion: {2} / fecha de medida de plazo: {3} / Nro de expediente: {4}"
    return txt.format(Self.Año, Self.Fecha_recepcion, Self.Fecha_medida_plazo, Self.Nro_expediente.expediente())

class localizacion(models.Model):
    Direccion = models.CharField(max_length=255, null=False, blank=False)
    Numero_calle = models.IntegerField(null=False, blank=False)
    Barrio = models.CharField(max_length=255, null=False, blank=False)
    DNI_victima = models.ForeignKey('victima', on_delete=models.CASCADE)
    DNI_agresor = models.ForeignKey('agresor', on_delete=models.CASCADE)
    DNI_niño = models.ForeignKey('niño', on_delete=models.CASCADE)
    Casa_de_proteccion = models.ForeignKey('casa_de_proteccion', on_delete=models.CASCADE)
    Red_de_contencion = models.ForeignKey('red_de_contencion', on_delete=models.CASCADE)

def __Str__(Self):
    txt = "Direccion: {1} / Numero y calle: {2} / Barrio: {3} / DNI victima: {4} / DNI agresor: {5} / DNI niño: {6} / Casa de proteccion: {7} / Red de contencion: {8}"
    return txt.format(Self.Direccion, Self.Numero_calle, Self.Barrio, Self.DNI_victima.dniVictima(), Self.DNI_agresor.dniAgresor(), Self.DNI_niño.dniNiño(), Self.Casa_de_proteccion.casaProteccion(), Self.Red_de_contencion.redContencion())

class denuncia(models.Model):
    Nro_expediente = models.ForeignKey('expediente', on_delete=models.CASCADE)
    Modalidad = models.ForeignKey('Modalidad', on_delete=models.CASCADE)
    caratula = models.ForeignKey('caratula', on_delete=models.CASCADE)

def __str__(Self):
    txt = "Nro de expediente: {1} / Modalidad: {2} / Caratula: {3}"
    return txt.format(Self.Nro_expediente.expediente(), Self.Modalidad.Violencia(), Self.caratula.Caratula())
    
