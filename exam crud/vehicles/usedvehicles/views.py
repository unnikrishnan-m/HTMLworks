from django.shortcuts import render, redirect

from django.views.generic import View

from usedvehicles.forms import UsedVehicleForm

from django.contrib import messages

from usedvehicles.models import UsedVehicle

# Create your views here.

class VehicleCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance = UsedVehicleForm()

        return render(request,"vehicle_create.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance = UsedVehicleForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"The vehicle is successfully added")

            return render(request,"vehicle_create.html",{"form":form_instance})
        else:

            messages.error(request,"the vehicle is not added")

            return render(request,"vehicle_create.html",{"form":form_instance})
    
class VehicleListView(View):

    def get(self,request,*args,**kwargs):

        

        qs = UsedVehicle.objects.all()

        return render(request,"vehicle_list.html",{"qs":qs})

class VehicleDetailView(View):

    def get(self,request,*args,**kwargs):

       

        id=kwargs.get("pk")

        qs = UsedVehicle.objects.get(id=id)

        return render(request,"vehicle_detail.html",{"qs":qs})
        

class VehicleUpdateView(View):

    def get(self,request,*args,**kwargs):

        
        
        id=kwargs.get("pk")

        qs=UsedVehicle.objects.get(id=id)

        form_instance = UsedVehicleForm(instance=qs)

        return render(request,"vehicle_update.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        veh_obj=UsedVehicle.objects.get(id=id)

        form_instance = UsedVehicleForm(request.POST,instance=veh_obj)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"vehicle updated successfully")
            
            return redirect("vehicle-list")
        else:

            messages.success(request,"vehicle updated successfully")

            return render(request,"vehicle_update.html",{"qs":veh_obj})

class VehicleDeleteView(View):

    def get(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        qs = UsedVehicle.objects.get(id=id).delete()

        return redirect("vehicle-list")




        

