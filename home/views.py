from django.shortcuts import render 
 
from django.http import HttpResponse #import response from dj 
 
def home(request): 
 
    peoples = [ 
        {"name": "John", "age":15}, 
        {"name": "Roman", "age":36}, 
        {"name": "Dean", "age":17}, 
        {"name": "Seth", "age":30}, 
        {"name": "San", "age":32} 
    ] 
 
    text = """ 
        Hello, world this is a testing of the django website work properly or not.Hello, world this is a testing of the django website work properly or not.Hello, world this is a testing of the django website work properly or not.Hello, world this is a testing of the django website work properly or not.Hello, world this is a testing of the django website work properly or not.Hello, world this is a testing of the django website work properly or not.Hello, world this is a testing of the django website work properly or not. 
    """ 
 
    vegetables = [ 
        "carrot", "Cucumber", "Tomato", "Potato" 
    ]  
 
    return render(request, "index.html", context={"page" : "Django Tutorial","peoples" : peoples, "text": text, "vegetables": vegetables}) 
 
def about(request): 
    context = {"page": "About"} 
    return render(request, "about.html", context) 
 
def contact(request): 
    context = {"page": "Contact"} 
    return render(request, "contact.html", context) 
 
 
def success_page(request): 
    print("*" * 10) 
    return HttpResponse("<h1>Hey This is a success page.</h1>")