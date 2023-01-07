from django.http import HttpResponse

def saludo(request):
    print("este es el el re", request.GET['numeros'] )
    lista_num = [int(num) for num in request.GET['numeros'].split(',')]
    print("la lista esta aqui", lista_num)
    new_lista = sorted(lista_num)
    #lista_num.sort()
    return HttpResponse(str(new_lista))

def mayor_edad(request, nombre, edad):
    if edad >=18:
        mensaje = f'Hola {nombre} puedes ingresar'
    else:
        mensaje = f'Hola {nombre} no puedes ingresar por que tienes {edad} años y eres menor de edad'
    return HttpResponse(mensaje)