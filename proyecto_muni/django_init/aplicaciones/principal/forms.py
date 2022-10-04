from pyexpat import model
from socket import fromshare
from django import forms
from .models import Modalidad, agresor, caratula, casa_de_proteccion, denuncia, expediente, informacion, localizacion, medida, periodo, red_de_contencion, victima, niño

class ModalidadForm(forms.ModelForm):
    class Meta:
        model = Modalidad
        fields = '__all__'


class caratulaForm(forms.ModelForm):
    class Meta:
        model = caratula
        fields = '__all__'

class victimaForm(forms.ModelForm):
    class Meta:
        model = victima
        fields = '__all__'


class agresorForm(forms.ModelForm):
    class Meta:
        model = agresor
        fields = '__all__'


class niñoForm(forms.ModelForm):
    class Meta:
        model = niño
        fields = '__all__'

class casa_de_proteccionForm(forms.ModelForm):
    class Meta:
        model = casa_de_proteccion
        fields = '__all__'

class red_de_contencionForm(forms.ModelForm):
    class Meta:
        model = red_de_contencion
        fields = '__all__'

class informacionForm(forms.ModelForm):
    class Meta:
        model = informacion
        fields = '__all__'

class expedienteForm(forms.ModelForm):
    class Meta:
        model = expediente
        fields = '__all__'

class medidaForm(forms.ModelForm):
    class Meta:
        model = medida
        fields = '__all__'

class periodoForm(forms.ModelForm):
    class Meta:
        model = periodo
        fields = '__all__'        

class localizacionForm(forms.ModelForm):
    class Meta:
        model = localizacion
        fields = '__all__'    

class denunciaForm(forms.ModelForm):
    class Meta:
        model = denuncia
        fields = '__all__'    
