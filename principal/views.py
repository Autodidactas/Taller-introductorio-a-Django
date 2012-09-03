from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from principal.models import Producto
from principal.forms import ProductoForm

def index(request):
	productos = Producto.objects.all().order_by('-id')
	return render_to_response("index.html", {"productos":productos}, context_instance=RequestContext(request))

def agregar_producto(request):
	if request.method == "POST":
		formulario = ProductoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/")
	else:
		formulario = ProductoForm()

	return render_to_response("agregar_productos.html", {"formulario":formulario}, context_instance=RequestContext(request))

def borrar_producto(request, id_producto):
	producto = Producto.objects.get(pk=id_producto)
	producto.delete()
	return HttpResponseRedirect("/")

def editar_producto(request, id_producto):
	producto = Producto.objects.get(pk=id_producto)
	if request.method == "POST":
		formulario = ProductoForm(request.POST, instance=producto)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/")
	else:
		formulario = ProductoForm(instance=producto)

	return render_to_response("editar_producto.html", {"formulario":formulario}, context_instance=RequestContext(request))