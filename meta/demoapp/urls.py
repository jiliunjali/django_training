from django.urls import path,re_path
from . import views # only '.' is required to symbol view file path as they both are in same directory...

urlpatterns = [
    path('', views.home, name='home'), #to have this path for any url after coming for this file : the url path should end with '/' -->http://127.0.0.1:8000/food/
    path('date/',views.display_date, name='display_date'),
    path('menu/', views.menu, name='menu'),
    path('getuser/<name>/<int:id>',views.pathview,name='pathview'),
    re_path(r'dish/(?P<item>[A-Za-z_]+)',views.card,name='card'), #?P is the syntax used to give name to capturing group and assign it to <item>
    path('home/',views.form_view, name='form_view'),
    path('login/',views.login_form_view),
    path('menuchart/',views.menu_modelform_view),
    path('reservation/',views.reservation_view),
    path('about/',views.about),
    path('table/',views.table),
    path('reserve/',views.reservation_display),
    #for inheritence practice
    path('hhome/',views._home),
    path('mmenu/',views._menu),
    path('aabout/',views._about),
    
    
    
    
    
]