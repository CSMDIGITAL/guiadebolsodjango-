from django.db import models

# Create your models here.
public class Associado(models);
     nome = models.CharField(max_length=100,null=false,blank=false)
     ativo = models.BooleanField(default=True,null=false,blank=false)
     def __str__(self):
         return self.name+" - Ativo: " + str(self.ativo)
     