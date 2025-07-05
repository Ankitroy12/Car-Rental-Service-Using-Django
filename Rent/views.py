from django.shortcuts import render
from django.shortcuts import HttpResponse
from Rent.models import Contact
from django.contrib import messages
def home(request):
   return render(request,'index.html')

def about(request):
   return render(request,'about.html')

def luxurious(request):
   return render(request,'luxurious.html')

def premium(request):
   return render(request,'premium.html')

def budget(request):
   return render(request,'budget.html')

def contact(request):
   car = request.GET.get('car')
   if request.method == "POST":
      name = request.POST.get('name')
      number = request.POST.get('number')
      address = request.POST.get('address')
      address2 = request.POST.get('address2')
      car = request.POST.get('car')
      day = request.POST.get('day')
      contact= Contact(name=name,number=number,address=address,address2=address2,car=car,day=day)
      contact.save()
      messages.success(request, "Thank you for choosing EliteRides! Your booking has been received, and our team will reach out to you shortly. We look forward to serving you!")
      
   return render(request,'contact.html',{'car': car})
                 
def bike(request):
   return render(request,'bike.html')