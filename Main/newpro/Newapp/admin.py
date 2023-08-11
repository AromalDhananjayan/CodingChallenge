from django.contrib import admin


from .models import City,Country

class City_admin(admin.ModelAdmin):
    list_display = ("Cityname","Citycode",)



admin.site.register(City,City_admin)
admin.site.register(Country)