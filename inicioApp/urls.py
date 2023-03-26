from django.urls import path
from inicioApp import views

urlpatterns = [
    path('', views.inicioDef,name='inicioUrl'),
    path('index/', views.indexDef,name='indexUrl'),
    path('pagina', views.paginaDef,name='paginaUrl'),
    path('loginAction/', views.loginSesionDef,name='loginUrl'),
    path('register/', views.registroDef,name='registerUrl'),
    path('registrarusuario/', views.registrarusuarios),
    path('gestion1/', views.gestionUser,name='registerpedidoUrl'),   
    path('registrarPedido/', views.registrarPedido),
    path('editarPedido/<codigo>', views.editarPedido),
    path('actualizarPedido/', views.actualizarPedido),
    path('eliminarPedido/<codigo>', views.eliminarPedido),
    path('buscar/', views.BuscarCliente),
    path('logout/', views.Salir, name='logout'),  
    path('tpizza/', views.tpizza, name='tpizza'),
    path('registrarpizza/', views.registrarPizza),
    path('fpago/', views.fpago, name='fpago'),
    path('registrarformapago/', views.registrarFormaPago),
    
]