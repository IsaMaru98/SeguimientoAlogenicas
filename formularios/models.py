from django.db import models

class Cosecha(models.Model):
    cci = models.CharField(max_length=10, default="")
    loteCosecha = models.CharField(default="", max_length=50)
    fechaCosecha = models.DateField()
    paseCosecha = models.CharField(choices=[('P0', 'P0'),('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3'), ('P4', 'P4'), ('P5', 'P5'), ('P6', 'P6'), ('P7', 'P7')] , max_length=10)
    areaFrascosCosecha = models.IntegerField(choices=[(25, 'T25'), (75, 'T75'), (175, 'T175'), (850, 'CR Liso'), (2125, 'CR Corrugado'), (0, 'Crioviales')]) 
    numFrascosCosecha = models.IntegerField()
    numCelulasObtenidas = models.FloatField()
    viabilidadCosecha = models.IntegerField()
    idCosecha = models.CharField(max_length=50, unique=True, primary_key=True)

    def save(self, *args, **kwargs): 
        self.idCosecha = self.generarIdCosecha()
        super().save(*args,*kwargs)

    def generarIdCosecha(self):
        return f"{self.cci}-{self.fechaCosecha}-{self.areaFrascosCosecha}-{self.numFrascosCosecha}-{self.loteCosecha}"

class Siembra(models.Model): 
    cci = models.CharField(max_length=10, default="")
    loteSimbra = models.CharField(max_length=50) 
    fechaSiembra = models.DateField()
    paseSiembra = models.CharField(max_length=50) 
    areaFrascosSiembra = models.IntegerField(choices=[(25, 'T25'), (75, 'T75'), (175, 'T175'), (850, 'CR Liso'), (2125, 'CR Corrugado'), (0, 'Crioviales')])
    numFrascosSiembra = models.IntegerField()
    numCelulasSembradasXFrasco = models.FloatField()
    cosechaFKSiembra = models.ForeignKey(Cosecha, on_delete=models.CASCADE)
    
     
class Crio(models.Model): 
    cci = models.CharField(max_length=10 , default="")
    numCelulasXVial = models.FloatField()
    numViales = models.IntegerField() 
    cosechaFKCrio = models.ForeignKey(Cosecha, on_delete=models.CASCADE, default="01-01-2000-25-1-001")







