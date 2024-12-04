from django import forms
from usedvehicles.models import UsedVehicle

class UsedVehicleForm(forms.ModelForm):

    class Meta:

        model = UsedVehicle

        fields = "__all__"

        widgets = {
            "title" : forms.TextInput(attrs={"class":"form-control"}),

            "owner_type" : forms.Select(attrs={"class":"form-control form-select"}),

            "running_kilometers" : forms.NumberInput(attrs={"class":"form-control"}),

            "price" : forms.TextInput(attrs={"class":"form-control"}),

            "fuel_type" : forms.Select(attrs={"class":"form-control form-select"})
        }