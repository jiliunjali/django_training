from django.db import models
from unicodedata import name

"""
the classes made in model can't be having instances in form class like : r=Reservation(), as they are storing tables and database and are not like callable function
else they will give TypeError
"""

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=100) #CharField used for small to large size string
    cuisine=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self): #to print objects of this class and table is our liked way inside queryset as it's elements
        return self.name + " "+self.cuisine+" "+self.price
    
class User(models.Model):
    id=models.IntegerField(primary_key=True)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    age=models.IntegerField()
    
    
#acc. to course 2 models are required : menucategory and menucard for menu of the resturant little lemon
class MenuCategory(models.Model):
    menu_category_name=models.CharField(max_length=200)
        
    
class MenuCard(models.Model):
    menu_item=models.CharField(max_length=100)
    price=models.IntegerField(null=False)
    cartegory_id=models.ForeignKey(
        MenuCategory,
        on_delete=models.PROTECT,
        default=None,
        related_name="category_name"
    )
    
#for modelform
class MenuChart(models.Model):
    dish=models.CharField(max_length=100)
    price=models.IntegerField(null=False)
    cuisine=models.CharField(max_length=100,help_text="enter what cuisine it is , eg: italian ")
    
#another example of modelform
class Reservation(models.Model):
    name=models.CharField(max_length=100, blank=True)
    contact=models.CharField('Phone Number',max_length=11)
    time=models.TimeField(auto_now_add=True)
    count=models.IntegerField()
    notes=models.CharField(max_length=300, blank=True)
    
    #inside the django admin portal used and mangeed by site manager , ther model entires are displayed as objects 
    # example: Reservation object (1)
    #to fix this as manager in future may not find it feasible, so vis str , we can change how entries look
    def __str__(self):
        return self.name
    
    
'''
need to specify in one model only
for one to one relationship ----models.OneToOneField()
for one to many or many to one ---models.ForeignKey()--written in one of them is enough [write the code in model whoes many objects are in relation with one]
for many to many --- models.ManyToManyField() ----can be written in either one
'''
    
# ---- library management system example
    
class Author(models.Model):
    name=models.CharField(max_length=50)
    
class Book(models.Model):
    title= models.CharField(max_length=100)
    author=models.ForeignKey(    #for one to many relationship ; book is many for a author
        Author,
        on_delete = models.CASCADE
    )

class Genre(models.Model):
    name=models.CharField(max_length=100)
    books=models.ManyToManyField( # many to many ; many book have many genres
        Book, 
        related_name = 'genres'
        ) 
    # related_name enables relation back to the model which is relation as other many ; it enables reverse relation and allow book 's object to access genres too
    
class BookCopyModel(models.Model):
    book_name=models.ForeignKey( #one to many ; a book , many copies
        Book,
        on_delete=models.CASCADE
    )
    copies=models.IntegerField()
    
class Member(models.Model):
    member_id=models.IntegerField( null=False, unique=True)
    name=models.CharField(max_length=200)
    borrowed_books=models.ManyToManyField( # many to many 
        Book,
        related_name='borrowers'
    )
    
class Borrow(models.Model):
    borrower=models.ForeignKey(
        Member,
        on_delete= models.CASCADE
    )
    borrow_date=models.DateTimeField()
    return_date=models.DateField()
    