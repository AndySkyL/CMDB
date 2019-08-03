from django.shortcuts import render, redirect, HttpResponse,reverse
from api import models


def business_unit(request):
    all_business_unit = models.BusinessUnit.objects.all()

    return render(request, 'business_unit.html', {'all_business_unit': all_business_unit})


from django import forms


class BusinessUnitForm(forms.ModelForm):
    class Meta:
        model = models.BusinessUnit     # 注意model 不能加s
        fields = "__all__"

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs.update({'class':'form-control'})

def business_unit_change(request,edit_id=None):
    obj = models.BusinessUnit.objects.filter(pk=edit_id).first()
    form_obj = BusinessUnitForm(instance=obj)
    if request.method == 'POST':
        form_obj = BusinessUnitForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('business_unit'))
    return render(request, 'form.html', {'form_obj': form_obj})
