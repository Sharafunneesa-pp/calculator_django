from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class AdditionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'add.html')
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get('num1')
        n2=request.POST.get('num2')
        result=int(n1)+int(n2)
        return render(request,'add.html',{"out":result})



class SubtractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get('num1')
        n2=request.POST.get('num2')
        result=int(n1)-int(n2)
        return render(request,'sub.html',{"res":result})
    

class MultiplicationView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"mult.html")
    
class DivisionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"div.html")

from functools import reduce   
class FactorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'fact.html')
    def post(self,request,*args,**kwargs):
        fact=1
        n=int(request.POST.get('num'))
        fact=reduce(lambda n1,n2:n1*n2,range(1,(n+1)))

        # for i in range(1,(n+1)):
        #     fact=(fact*i)
        return render(request,'fact.html',{'result':fact})   


class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')    

