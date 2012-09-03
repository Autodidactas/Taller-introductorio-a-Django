from django import forms
from principal.models import Producto

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto