from django.contrib import admin
from .models import Modalidad
from .models import caratula
from .models import victima
from .models import agresor
from .models import niño
from .models import casa_de_proteccion
from .models import red_de_contencion
from .models import informacion
from .models import expediente
from .models import medida
from .models import periodo
from .models import localizacion
from .models import denuncia
admin.site.register(Modalidad)
admin.site.register(caratula)
admin.site.register(victima)
admin.site.register(agresor)
admin.site.register(niño)
admin.site.register(casa_de_proteccion)
admin.site.register(red_de_contencion)
admin.site.register(informacion)
admin.site.register(expediente)
admin.site.register(medida)
admin.site.register(periodo)
admin.site.register(localizacion)
admin.site.register(denuncia)

# Register your models here.
