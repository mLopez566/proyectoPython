from django.contrib import admin

# Register your models here.
from .models import raza, upp, ranch, animal

admin.site.register(raza)
admin.site.register(upp)
admin.site.register(ranch)
admin.site.register(animal)

