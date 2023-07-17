from django.http import HttpResponse
from django.template import Template, Context, loader
from mi_app_1.models import Familiar

def mi_template(request):
    plantilla = loader.get_template("index.html")
    datos = {
        "nombre": "Joel",
        "apellido": "Miranda",
        "dni": 36766935,
    }
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def mostrar_familiares(pnombre, papellido, pdni, pfecha_nac, pemail):
    familiar = Familiar(nombre = pnombre, apellido = papellido, dni = pdni, fecha_nac = pfecha_nac, email = pemail)
    familiar.save()
    respuesta = f"El familiar agregado es: {familiar.nombre} {familiar.apellido}<br>DNI: {familiar.dni}<br>FECHA DE NACIMIENTO: {familiar.fecha_nac}<br>EMAIL: {familiar.email}"
    familiar2 = Familiar("Melisa","Miguez",36988123,26/3/1993,"Mm@gmail.com")
    familiar2.save()
    familiar3 = Familiar("Zoe","Miranda",53698745,28/7/2010,)
    familiar3.save()
    respuesta2 = f"_______________________________________________Resto de la familia: <br> NOMBRE Y APELLIDO: {familiar2.nombre} {familiar2.apellido}<br>DNI: {familiar2.dni}<br>FECHA DE NACIMIENTO: {familiar2.fecha_nac}<br>EMAIL: {familiar2.email}"
    respuesta3 = f"_______________________________________________<br> NOMBRE Y APELLIDO: {familiar3.nombre} {familiar3.apellido}<br>DNI: {familiar3.dni}<br>FECHA DE NACIMIENTO: {familiar3.fecha_nac}<br>EMAIL: {familiar3.email}"
    return HttpResponse(respuesta, respuesta2, respuesta3)