from django.db import models
import math as ma
class Siembra(models.Model):
    cci = models.CharField(max_length=10, default="")
    medioSiembra = models.CharField(max_length=50, default="NR", editable=True)
    loteSimbra = models.CharField(max_length=50)
    fechaSiembra = models.DateField()
    paseSiembra = models.CharField(choices=[('P0', 'P0'),('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3'), ('P4', 'P4'), ('P5', 'P5'), ('P6', 'P6'), ('P7', 'P7')] , max_length=10)
    areaFrascosSiembra = models.IntegerField(choices=[(25, 'T25'), (75, 'T75'), (175, 'T175'), (850, 'CR Liso'), (2125, 'CR Corrugado'), (1272, 'CS 2p'), (3180, 'CS 5p'), (6360, 'CS 10p'), (500, 'TripleFlask'),  (0, 'Crioviales')])
    numFrascosSiembra = models.IntegerField()
    numCelulasSembradasXFrasco = models.FloatField()
    densidadSiembra = models.IntegerField()
    siembraId = models.CharField(max_length=50, unique=True, primary_key=True)
    totalSiembra = models.FloatField(max_length=10)

    def save(self, *args, **kwargs):
        self.siembraId = self.generarSiembraId()
        self.densidadSiembra = self.generarDensidadSiembra()
        self.totalSiembra = self.generarTotalSiembra()
        super(Siembra, self).save(*args,*kwargs)

    def generarDensidadSiembra(self):
        r = (self.numCelulasSembradasXFrasco*1000000)/ self.areaFrascosSiembra
        densidadSiembra = round(r,2)
        return densidadSiembra

    def generarSiembraId(self):
        return f"{self.cci}-{self.loteSimbra}-{self.paseSiembra}-{self.fechaSiembra}-{self.areaFrascosSiembra}-{self.numFrascosSiembra}"

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
    areaFrascosCosecha = models.IntegerField(choices=[(25, 'T25'), (75, 'T75'), (175, 'T175'), (850, 'CR Liso'), (2125, 'CR Corrugado'),(1272, 'CS 2p'), (3180, 'CS 5p'), (6360, 'CS 10p'), (500, 'TripleFlask'), (0, 'Crioviales')])
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
        super(Cosecha, self).save(*args,*kwargs)

    def generarTotalObtenidas(self):
        r = self.numCelulasObtenidas * 1000000
        totalObtenidas = round(r,2)
        return totalObtenidas

    def generarIdCosecha(self):
        return f"{self.cci}-{self.loteCosecha}-{self.paseCosecha}-{self.fechaCosecha}-{self.areaFrascosCosecha}-{self.numFrascosCosecha}"

    def generarDensidadCosecha(self):
        r = ((self.numCelulasObtenidas*1000000)/(self.areaFrascosCosecha*self.numFrascosCosecha))
        densidadCosecha = round(r, 2 )

        return densidadCosecha

    def __str__(self):
        return self.cosechaId


class Crio(models.Model):
    cosecha = models.ForeignKey(Cosecha, on_delete=models.CASCADE)
    cci = models.CharField(max_length=10 , default="")
    numCelulasXVial = models.FloatField()
    numViales = models.IntegerField()
    totalCrio = models.IntegerField()
    crioId = models.CharField(max_length=50, unique=True, primary_key=True)
    fechaCrio = models.DateField()

    def save(self, *args, **kwargs):
        self.totalCrio = self.generarTotalCrio()
        self.crioId = self.generarCrioId()
        super(Crio, self).save(*args,*kwargs)

    def generarCrioId(self):
        return f"{self.cci}-{self.cosecha.loteCosecha}-{self.cosecha.paseCosecha}-{self.fechaCrio}-{self.cosecha.areaFrascosCosecha}-{self.cosecha.numFrascosCosecha}"

    def generarTotalCrio(self):

        r =  round((self.numCelulasXVial * self.numViales), 2)

        return r

    def __str__(self):
        return self.crioId


class Dato(models.Model):
    cci = models.CharField(max_length=10 , default="")
    siembra = models.ForeignKey(Siembra, on_delete=models.CASCADE)
    cosecha = models.ForeignKey(Cosecha, on_delete=models.CASCADE)
    loteDatos = models.CharField(default="000", max_length=50)
    pase = models.CharField(default="000", max_length=50)
    densidadCosecha = models.FloatField(default=0.0,  max_length=10)
    densidadSiembra = models.FloatField(default=0.0,  max_length=10)
    medioSiembra = models.CharField(max_length=50 , default="NR", editable=True)
    generaciones = models.FloatField()
    tiempoDuplicacion = models.FloatField()
    relacionExpansion = models.FloatField()
    comentarios = models.CharField(max_length=100 , default="")



    datoId = models.CharField(max_length=50, primary_key=True)

    def save(self,*args,**kargs):
        #Definir valores traidos de siembra y cosecha
        self.loteDatos = self.siembra.loteSimbra
        self.medioSiembra = self.siembra.medioSiembra
        self.pase = self.siembra.paseSiembra
        self.densidadCosecha = self.cosecha.densidadCosecha
        self.densidadSiembra = self.siembra.densidadSiembra

        # Generar id de Dato
        self.datoId = self.generarDatoId()

        #Definir valores necesarios para los calculos
        totalSembradas = self.siembra.totalSiembra
        totalObtenidas = self.cosecha.totalObtenidas
        relacionExpansion = round((totalObtenidas/totalSembradas),2)
        diasCultivo = self.cosecha.tiempoCultivoDias
        X = ma.log(relacionExpansion)

        # Asociar valores a los campos del modelo
        self.generaciones = round(X/ma.log(2), 2)
        self.tiempoDuplicacion = round(diasCultivo* (ma.log(2)/X) , 2)
        self.relacionExpansion = relacionExpansion

        super(Dato,self).save(*args,**kargs)

    def generarDatoId(self):
        return f"{self.cci}-{self.cosecha.loteCosecha}-{self.cosecha.paseCosecha}-{self.cosecha.fechaCosecha}-{self.cosecha.areaFrascosCosecha}-{self.cosecha.numFrascosCosecha}"


    def __str__(self):
        return self.datoId







