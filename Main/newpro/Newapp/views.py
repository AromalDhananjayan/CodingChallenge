from django.shortcuts import render

from django.template import loader

from django.http import HttpResponse

from .models import City

from .form import _City

def members(request):
    template= loader.get_template("main.html")
    return HttpResponse(template.render())


def check_user(request):
    if request.method == 'POST':
        form = _City(request.POST)
        if form.is_valid():
            Cityname = form.cleaned_data['Cityname']
            try:
                user = City.objects.get(Cityname=Cityname)
                exists_in_db = True
            except City.DoesNotExist:
                exists_in_db = False
            return render(request, 'result.html', {'exists_in_db': exists_in_db, 'Cityname': Cityname})
    else:
        form = _City()
    return render(request, 'check_user.html', {'form': form})
