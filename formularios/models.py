from django.db import models

class Cosecha(models.Model):
    loteCosecha = models.CharField(default="", max_length=50)
    fechaCosecha = models.DateField()
    paseCosecha = models.CharField(max_length=50)
    areaFrascosCosecha = models.IntegerField(choices=[(25, 'T25'), (75, 'T75'), (175, 'T175'), (850, 'CR Liso'), (2125, 'CR Corrugado'), (0, 'Crioviales')]) 
    numFrascosCosecha = models.IntegerField()
    numCelulasObtenidas = models.FloatField()
    viabilidadCosecha = models.IntegerField()
    idCosecha = models.CharField(max_length=50, unique=True, primary_key=True)

    def save(self, *args, **kwargs): 
        self.idCosecha = self.generarIdCosecha()
        super().save(*args,*kwargs)

    def generarIdCosecha(self):
        return f"{self.fechaCosecha}-{self.areaFrascosCosecha}-{self.numFrascosCosecha}-{self.loteCosecha}"

class Siembra(models.Model): 
    loteSimbra = models.TextField() 
    fechaSiembra = models.DateField()
    paseSiembra = models.TextField()
    areaFrascosSiembra = models.IntegerField(choices=[(25, 'T25'), (75, 'T75'), (175, 'T175'), (850, 'CR Liso'), (2125, 'CR Corrugado'), (0, 'Crioviales')])
    numFrascosSiembra = models.IntegerField()
    numCelulasSembradasXFrasco = models.FloatField()
    cosechaFK = models.ForeignKey(Cosecha, on_delete=models.CASCADE)
    
     
class Crio(models.Model): 
    numCelulasXVial = models.FloatField()
    numViales = models.IntegerField() 


