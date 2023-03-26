from django.shortcuts import render,redirect
from .models import Usuario
from django.contrib import messages
from .models import Pedidos,tipopizza, formapago
from django.http import HttpResponse
from django.contrib.auth import logout
from django.core.cache import cache

# Create your views here.
def inicioDef(request):
    return render(request, 'index.html',{})

def indexDef(request):
    cliente = cache.get('cliente')
    pedidosListados = Pedidos.objects.all()    
    tpizza = tipopizza.objects.all()
    fpago = formapago.objects.all()
    return render(request, "gestionpedidos.html",{"cliente": cliente,"pedidos": pedidosListados, "mypizza" : tpizza, "mfpago" : fpago})

def paginaDef(request):
    return render(request,'Pagina.html', {})

def loginSesionDef(request):    
    if request.method == 'GET':
        return render(request, 'index.html', {})
    else:
        usuarioStr = request.POST.get('txtuser')
        claveStr = request.POST.get('txtpass')                               

        try:
            usuario = Usuario.objects.get(usuario=usuarioStr)
            pedidosListados = Pedidos.objects.all()    
            tpizza = tipopizza.objects.all()
            fpago = formapago.objects.all()
            if usuario.contrasena == claveStr:
                nombre_usuario = usuario.nombre
                cache.set('cliente', nombre_usuario)
                return render(request, "gestionpedidos.html",{"usuarioStr": usuario.usuario,"cliente": nombre_usuario,"pedidos": pedidosListados, "mypizza" : tpizza, "mfpago" : fpago})
            #   return redirect('pedidosadmin',{"usuarioStr": usuario.usuario,"cliente": nombre_cliente})
            else:
                return render(request, "index.html", {"err": "La contraseña es incorrecta."})
        except Usuario.DoesNotExist:
            return render(request, "index.html", {"err": "El usuario no existe."})
        
def registroDef(request):
    return render(request,'registrouser.html', {})

def registrarusuarios(request):
    
    myuser=request.POST['txtuser']
    myname=request.POST['txtname']
    mypass=request.POST['txtpass']
    
    try:
        Usuario.objects.create(usuario=myuser, contrasena=mypass, nombre=myname)
    except:
        messages.error(request, 'Ha ocurrido un error.')    
        return render(request, 'registrouser.html', {'mensaje_tipo': 'error',
                                                    'mensaje_texto': 'Ha ocurrido un error.'})
    else:
        messages.success(request, 'Registro exitoso.')
        return render(request, 'registrouser.html',
                      {'mensaje_tipo': 'success', 'mensaje_texto': 'Registro exitoso.'})

    



def registrarPedido(request):
    mycli=request.POST['txtcliente']
    mytpizza=request.POST['mpizza']
    myfpago=request.POST['mpago']
    mycant=request.POST['txtcant']
    myprecio=request.POST['txtprecio']
    mytotal=request.POST['total_ventas']

    tipo_pizza = tipopizza.objects.get(idtipopizza=mytpizza)
    tipo_pago = formapago.objects.get(idformapago=myfpago)
    
    t_pago= float(mytotal)    
    Pedidos.objects.create(cliente=mycli, tipopizza=tipo_pizza,formapago=tipo_pago,cantidad=mycant,precio=myprecio,total=t_pago)
    
    return redirect("indexUrl")

def editarPedido(request, codigo):    
    pedido = Pedidos.objects.get(codigo=codigo)
    tpizza = tipopizza.objects.all()
    fpago = formapago.objects.all()
    cliente = cache.get('cliente')

    return render(request, "editarPedido.html", {"pedido": pedido,"mypizza" : tpizza, "mfpago" : fpago, "cliente": cliente})

def actualizarPedido(request):
    mcod=request.POST['txtcodigo']
    mcli=request.POST['txtcliente']
    mtipo=request.POST['tipopizza']
    mpago=request.POST['formapago']
    mcant=request.POST['txtcant']
    mprecio=request.POST['txtprecio']
    mtotal=request.POST['total_ventas']

    tipo_pizza = tipopizza.objects.get(idtipopizza=mtipo)
    tipo_pago = formapago.objects.get(idformapago=mpago) 

    numero_con_punto = mtotal.replace(',', '.')
    t_pago = float(numero_con_punto)

    pedido = Pedidos.objects.get(codigo=mcod)
    pedido.cliente = mcli
    pedido.tipopizza = tipo_pizza
    pedido.formapago = tipo_pago
    pedido.precio = mprecio
    pedido.cantidad = mcant
    pedido.total = t_pago
    pedido.save()    
    return redirect("indexUrl")

  

def eliminarPedido(request, codigo):
    pedido = Pedidos.objects.get(codigo=codigo)
    pedido.delete()    

    return redirect("indexUrl")

def gestionUser(request):
    pedidosListados = Pedidos.objects.all()    
    tpizza = tipopizza.objects.all()
    fpago = formapago.objects.all()   
    cliente = cache.get('cliente')

    return render(request, "registrarPedido.html", {"pedidos": pedidosListados, "mypizza" : tpizza, "mfpago" : fpago, "cliente": cliente})

def BuscarCliente(request):
    cliente = cache.get('cliente')
    cliente1 = request.GET.get("pBuscar")
    if cliente1:
        resultados = Pedidos.objects.filter(cliente__icontains=cliente1)
        if resultados.exists():
            return render(request, 'gestionpedidos.html', {'pedidos': resultados, 'busqueda': cliente1, 'cliente': cliente})
        else:
            mensaje = 'No se encontraron resultados para la búsqueda: ' + cliente1
            return HttpResponse(mensaje)
    else:
        pedidos = Pedidos.objects.all()
        return render(request, 'gestionpedidos.html', {'pedidos': pedidos, 'cliente': cliente})


def Salir(request):
    logout(request)
    return redirect('/')

def tpizza(request):
    cliente = cache.get('cliente')
    return render(request,'regtipopizza.html',{"cliente":cliente})

def registrarPizza(request):
    tipo=request.POST['txtpizza']
    tipopizza.objects.create(descripcion=tipo)
    return redirect("tpizza")

def fpago(request):
    cliente = cache.get('cliente')
    return render(request,'regfpago.html', {"cliente":cliente})

def registrarFormaPago(request):
    tipo=request.POST['txtfpago']
    formapago.objects.create(descripcion=tipo)
    return redirect("fpago")

    





        
            