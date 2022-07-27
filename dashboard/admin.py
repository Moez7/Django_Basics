from django.contrib import admin
from .models import Groupe, BaseReseauCommerciaux, Indicateurs, RealisationPilotage

# Register your models here.

admin.site.register(Groupe)
admin.site.register(BaseReseauCommerciaux)
admin.site.register(Indicateurs)
admin.site.register(RealisationPilotage)

