from django.shortcuts import render
from gymapp.forms import User_Form

# Create your views here.
def index(request):
    return render(request,'Index.html')

def about(request):
    return render(request,'About.html')

def form(request):
    form=User_Form()
    return render(request,"Registration_Form.html",{'uform':form})