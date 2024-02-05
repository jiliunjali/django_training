from django.shortcuts import render
from django.http import HttpResponse # by me
from datetime import datetime

from .forms import InputForm, loginFormEx, MenuForm, ReservationForm
from .models import Reservation

# Create your views here.
def home(request):
    return HttpResponse("Wecome to LittleLemon restaurant ! ")

def display_date(request):
    date_to_display = datetime.today().year
    return HttpResponse(date_to_display)

# to print attributes of httprequest object 
def menu(request):
    # text='''<h1 style="color:#F4CE14;">"you are inside menu of LittleLemon restaurant"</h1>'''
    # return HttpResponse(text)
    path = request.path 
    method = request.method
    scheme =request.scheme
    address=request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info=request.path_info
    msg=f'''<br>
            <br>path = {path} 
            <br>method = {method}
            <br>scheme ={scheme}
            <br>address={address}
            <br>user_agent = {user_agent}
            <br>path_info={path_info}
    
    '''
    content=''' 
            <center><h2>Testing Django Request Response Objects</h2> 
            <p>Request path : " {}</p> 
            <p>Request Method :{}</p></center> 
            '''.format(path, method) 
    return HttpResponse(msg, content_type='text/html',charset='utf-8')

# to understand how to handle and work with url parameters which are passed
#parameters need to be taken as argument by this function as they are added inside path() of urls.py of app 
def pathview(request, name, id):
    return HttpResponse(f"Name:{name}, Id: {id}")

def card(request, item):
    food_menu = {
    'spring_rolls': {'name': 'Spring Rolls', 'price': 5.99},
    'bruschetta': {'name': 'Bruschetta', 'price': 7.49},
    'chicken_wings': {'name': 'Chicken Wings', 'price': 8.99},
    'spaghetti_bolognese': {'name': 'Spaghetti Bolognese', 'price': 12.99},
    'grilled_salmon': {'name': 'Grilled Salmon', 'price': 15.99},
    'vegetarian_pizza': {'name': 'Vegetarian Pizza', 'price': 11.99},
    'chocolate_cake': {'name': 'Chocolate Cake', 'price': 6.99},
    'fruit_salad': {'name': 'Fruit Salad', 'price': 4.99},
    'cheesecake': {'name': 'Cheesecake', 'price': 8.49},
    'soda': {'name': 'Soda', 'price': 2.49},
    'iced_tea': {'name': 'Iced Tea', 'price': 1.99},
    'coffee': {'name': 'Coffee', 'price': 3.49},
    }

    dish=food_menu[item]
    return HttpResponse(f"<h2>{item}</h2> Name: {dish['name']}, Price: {dish['price']}")
    # return HttpResponse(f"<h2>{item}</h2> "+str(dish))  #httpresponse work with text or html, dict can't be appended with string
    
#for my form 
def form_view(request):
    print("form_view function is called!")
    form =InputForm()
    context={"form": form}
    return render(request, "home.html", context)

def login_form_view(request):
    form=loginFormEx()
    context={"form":form}
    return render(request, "login.html",context)

#form_view and login_view are the simple views with form || for form which is model form we need to add some functioning special to such form
def menu_modelform_view(request):
    form=MenuForm() # to create empty instance of our form class that we have made
    if request.method == "POST":
        form=MenuForm(request.POST) # it will update the form obj with request.post || by doing so we bind form with POST data
        if form.is_valid():
            form.save()
    context={"form":form}
    return render(request, "menuchart.html",context)

def reservation_view(request):
    form=ReservationForm()
    if request.method ==  "POST":
        form=ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    context={"form":form}
    return render(request, "menuchart.html",context)

def about(request):
    about_content={'about':'<h1>Welcome to Little Lemon Restaurant</h1><br>At Little Lemon, we believe in bringing you the freshest and most delicious flavors in every dish.<br>From mouthwatering appetizers to delectable desserts, we strive to delight your taste buds with our culinary creations.'}
    return render(request,"about.html",about_content)

# forpracticing forloop tag in dtl
def table(request):
    content={'mains':[{'name':'pasta','price':'2434'},
                    {'name':'ice-cream','price':'34'},
                    {'name':'maggi','price':'434'},
                    {'name':'fries','price':'243'}
                    ]}
    return render(request, 'table.html',content)

# for template with model
def  reservation_display(request):
    data=Reservation.objects.all()
    list_data={'list':data}
    return render(request,'reservation.html',list_data)

#for template inheritance
def _home(request):
    return render(request,'_index.html')

def _about(request):
    return render(request,'_about.html')

def _menu(request):
    return render(request,'_menu.html')