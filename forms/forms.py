from django import forms
from .models import *

class Form1(forms.ModelForm):
    class Meta:
        model = ModelForm1
        fields = ["name" ,  "address" , "age" , "roomNumber" , "gender" , "phonenumber" , "nationalId" ]
        labels  = {
        "name"       : "" ,
        "nationalId" : "" ,
        "address"    : "" ,
        "age"        : "" ,
        "roomNumber" : "" ,
        "gender"     : "" ,
        "phonenumber": "" ,
        "nationalId" : ""
        # "exitDate" : "" ,
        }
        widgets = {
        'name'       : forms.TextInput(attrs  = {'class':'form-control' , "placeholder" : "أسم المريض"})  ,
        'nationalId' : forms.TextInput(attrs  = {'class':'form-control' , "placeholder" : "الرقم القومى"}),
        'age'        : forms.TextInput(attrs  = {'class':'form-control' , 'placeholder' : 'عمر المريض'})  ,
        'address'    : forms.TextInput(attrs  = {'class':'form-control' , 'placeholder' : 'العنوان'})  ,
        'roomNumber' : forms.TextInput(attrs  = {'class':'form-control' , 'placeholder' : 'رقم الغرفه'})  ,
        'phonenumber': forms.TextInput(attrs  = {'class':'form-control' , 'placeholder' : 'رقم الهاتف'}) ,
        'gender'     : forms.TextInput(attrs  = {'class':'form-control' , 'placeholder' : 'النوع' }) ,
        # 'exitDate'   : forms.TextInput(attrs  = {'class':'form-control' , 'placeholder' : 'وقت الخروج' })
        }

class Form2(forms.ModelForm):
    class Meta:
        model = ModelForm2
        fields = ['forigenKey' , 'drdep' , 'department' , 'Diagnosis']
        labels  = {
        "forigenKey" : "" ,
        "drdep"      : "" ,
        "department" : "" ,
        "Diagnosis"  : ""
        }
        widgets = {
        'drdep'      : forms.TextInput(attrs = {'class':'form-control' , "placeholder" : "وحدة الاستاذ الدكتور"})  ,
        'department' : forms.TextInput(attrs = {'class':'form-control' , 'placeholder' : ' القسم المحول أليه'}) ,
        'Diagnosis'  : forms.TextInput(attrs = {'class':'form-control' , 'placeholder' : 'التشخيص'})  ,
        }
