from django.shortcuts import render
from . import forms

def form_page(request):
    form=forms.NameForm
    if request.method=='POST':
        form=forms.NameForm(request.POST)
        if form.is_valid():
            print("Validation Success!")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
    return render(request,'validform/formpage.html', {'form':form})
# Create your views here.
