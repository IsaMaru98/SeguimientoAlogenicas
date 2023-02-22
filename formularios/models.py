from django.db import models
import math as ma 
class Siembra(models.Model): 
    cci = models.CharField(max_length=10, default="")
    loteSimbra = models.CharField(max_length=50) 
    fechaSiembra = models.DateField()
    paseSiembra = models.CharField(choices=[('P0', 'P0'),('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3'), ('P4', 'P4'), ('P5', 'P5'), ('P6', 'P6'), ('P7', 'P7')] , max_length=10)
    areaFrascosSiembra = models.IntegerField(choices=[(25, 'T25'), (75, 'T75'), (175, 'T175'), (850, 'CR Liso'), (2125, 'CR Corrugado'), (0, 'Crioviales')])
    numFrascosSiembra = models.IntegerField()
    numCelulasSembradasXFrasco = models.FloatField()
    densidadSiembra = models.IntegerField()
    siembraId = models.CharField(max_length=50, unique=True, primary_key=True)
    totalSiembra = models.FloatField(max_length=10)

    def save(self, *args, **kwargs): 
        self.siembraId = self.generarSiembraId()
        self.densidadSiembra = self.generarDensidadSiembra()
        self.totalSiembra = self.generarTotalSiembra()
        super().save(*args,*kwargs)
    
    def generarDensidadSiembra(self): 
        r = (self.numCelulasSembradasXFrasco*1000000)/ self.areaFrascosSiembra
        densidadSiembra = round(r,2)
        return densidadSiembra

    def generarSiembraId(self):
        return f"{self.cci}-{self.fechaSiembra}-{self.areaFrascosSiembra}-{self.numFrascosSiembra}-{self.loteSimbra}"
    
    def generarTotalSiembra(self): 
        r = self.numCelulasSembradasXFrasco * 1000000 * self.numFrascosSiembra 
        totalSiembra = round(r, 2)
        return totalSiembra 

    def __str__(self): 
        return self.siembraId


class Cosecha(models.Model):
    cci = models.CharField(max_length=10, default="")
    loteCosecha = models.CharField(default="", max_length=50)
    fechaCosecha = models.DateField()
    paseCosecha = models.CharField(choices=[('P0', 'P0'),('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3'), ('P4', 'P4'), ('P5', 'P5'), ('P6', 'P6'), ('P7', 'P7')] , max_length=10)
    areaFrascosCosecha = models.IntegerField(choices=[(25, 'T25'), (75, 'T75'), (175, 'T175'), (850, 'CR Liso'), (2125, 'CR Corrugado'), (0, 'Crioviales')]) 
    numFrascosCosecha = models.IntegerField()
    confluenciaCosecha = models.FloatField()
    tiempoCultivoDias = models.IntegerField()
    numCelulasObtenidas = models.FloatField()
    viabilidadCosecha = models.IntegerField()
    siembra = models.ForeignKey(Siembra, on_delete=models.CASCADE)
    densidadCosecha = models.IntegerField()
    totalObtenidas = models.FloatField()
    cosechaId = models.CharField(max_length=50, unique=True, primary_key=True)


    def save(self, *args, **kwargs): 
        self.densidadCosecha = self.generarDensidadCosecha()
        self.totalObtenidas = self.generarTotalObtenidas()
        self.cosechaId = self.generarIdCosecha()
        super().save(*args,*kwargs)

    def generarTotalObtenidas(self):
        r = self.numCelulasObtenidas * 1000000 
        totalObtenidas = round(r,2) 
        return totalObtenidas 

    def generarIdCosecha(self):
        return f"{self.cci}-{self.fechaCosecha}-{self.areaFrascosCosecha}-{self.numFrascosCosecha}-{self.loteCosecha}"

    def generarDensidadCosecha(self): 
        r = ((self.numCelulasObtenidas*1000000)/(self.areaFrascosCosecha*self.numFrascosCosecha))
        densidadCosecha = round(r, 2 )

        return densidadCosecha

    def __str__(self): 
        return self.cosechaId


class Crio(models.Model): 
    cci = models.CharField(max_length=10 , default="")
    numCelulasXVial = models.FloatField()
    numViales = models.IntegerField() 
    totalCrio = models.IntegerField()

    def save(self, *args, **kwargs): 
        self.totalCrio = self.generarTotalCrio()
        super().save(*args,*kwargs)

    def generarTotalCrio(self):

        r =  round((self.numCelulasXVial * self.numViales), 2)

        return r


class Dato(models.Model): 
    siembra = models.ForeignKey(Siembra, on_delete=models.CASCADE)
    cosecha = models.ForeignKey(Cosecha, on_delete=models.CASCADE)
    generaciones = models.FloatField()
    tiempoDuplicacion = models.FloatField()
    relacionExpansion = models.FloatField() 

    def save(self,*args,**kargs):
        totalSembradas = self.siembra.totalSiembra 
        totalObtenidas = self.cosecha.totalObtenidas
        relacionExpansion = round((totalObtenidas/totalSembradas),2)
        diasCultivo = self.cosecha.tiempoCultivoDias
        X = ma.log(relacionExpansion)

        self.generaciones = round(X/ma.log(2), 2)
        self.tiempoDuplicacion = round(diasCultivo* (ma.log(2)/X) , 2)
        self.relacionExpansion = relacionExpansion

        return super().save(*args,**kargs)






