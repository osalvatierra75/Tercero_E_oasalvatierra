from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=20, null=False, blank=False,unique=True)
    contrasena = models.CharField(max_length=20, null=False, blank=False)
    nombre = models.CharField(max_length=70, null=False, blank=False)

class tipopizza(models.Model):
    idtipopizza=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        tpizza= "{0} ({1})"
        return tpizza.format(self.idtipopizza,self.descripcion)
    
    
    

class formapago(models.Model):
    idformapago=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=40,null=False,blank=False)

    def __str__(self):
        fpago= "{0} ({1})"
        return fpago.format(self.idformapago,self.descripcion)

class Pedidos(models.Model):
    codigo = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=70)
    tipopizza = models.ForeignKey(tipopizza,null=False,blank=False, on_delete=models.CASCADE,related_name="fk_tipopizza",db_column="idtipopizza")
    formapago = models.ForeignKey(formapago,null=False,blank=False, on_delete=models.CASCADE,related_name="fk_formapago",db_column="idformapago")
    cantidad = models.IntegerField(null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    total = models.DecimalField(max_digits=10, decimal_places=2,null=False, blank=False)

    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.cliente,self.tipopizza,self.formapago,self.cantidad, self.precio, self.total)