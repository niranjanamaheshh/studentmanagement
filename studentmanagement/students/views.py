from django.shortcuts import render,redirect
from django.views import View
from .forms import *
from django.contrib.auth import authenticate
from .models import Students
from django.contrib import messages

# Create your views here.
 
class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'index.html',{"form":form})
    def post(self,request):
        formdata=LoginForm(data=request.POST)
        if formdata.is_valid():
            usrnm=formdata.cleaned_data.get('username')
            pswd=formdata.cleaned_data.get('password')
            user=authenticate(request,username=usrnm,password=pswd)
            if user:
                return redirect('landing')
            else:
                return redirect('login')
    
class SignUpview(View):
    def get(self,request):
        form=SignUpForm()
        return render(request,"signup.html",{"form":form})
    def post(self,request):
        formdata=SignUpForm(data=request.POST)
        if formdata.is_valid():
            formdata.save()
            messages.success(request,"Registration Successfull!!")
            return redirect('login')
        messages.error(request,"Registration Failed")
        return render(request,"signup.html",{"form":formdata})
        
class LandingView(View):
    def get(self,request):
        return render(request,'landing.html')
    
class AddStudentView(View):
    def get(self,request):
        form=StudentModelForm()
        return render(request,'addstudents.html',{"form":form})
    def post(self,request):
        formdata=StudentModelForm(data=request.POST,files=request.FILES)
        if formdata.is_valid():
            formdata.save()
            messages.success(request,"Student Added Successfully!!")
            return redirect('view')
        messages.error(request,"Invalid Data")
        return render(request,"addstudents.html",{"form":formdata})
    
class ViewStudentsView(View):
    def get(self,request):
        data=Students.objects.all()
        return render(request,'viewstudents.html',{"data":data})
    
class EditStudentView(View):
    def get(self,request,**kwargs):
        sid=kwargs.get('id')
        student=Students.objects.get(id=sid)
        form=StudentModelForm(instance=student)
        return render(request,'editstudent.html',{"form":form})
    def post(self,request,**kwargs):
        sid=kwargs.get('id')
        student=Students.objects.get(id=sid)
        formdata=StudentModelForm(data=request.POST,files=request.FILES,instance=student)
        if formdata.is_valid():
            formdata.save()
            messages.success(request,"Updated Successfully")
            return redirect('view')
        messages.error(request,"Checking")
        return render(request,'editstudent.html',{"form":formdata})
    
class DeleteStudentView(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get('id')
        print('tid')
        task=Students.objects.get(id=sid)
        task.delete()
        messages.success(request,"Deleted Successfully")
        return redirect('view')