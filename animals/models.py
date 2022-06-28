from django.db import models

# Create your models here.

class ranch(models.Model):
    name_r = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name_r

class upp(models.Model):
    num = models.IntegerField(unique=True)
    name_u = models.CharField(max_length=255)
    prop = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.num

class raza(models.Model):
    raza = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.raza

class animal(models.Model):
    arete = models.IntegerField(unique=True)
    upp = models.ForeignKey(upp, on_delete=models.CASCADE)
    raza = models.ForeignKey(raza, on_delete=models.CASCADE)
    edad = models.IntegerField()
    ubication = models.ForeignKey(ranch, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.arete