from django.contrib import admin
from shoping.models import *

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ['typ','name','index','west_east']
    search_fields = ['typ','name','index','west_east']
    list_filter = ['typ','name','index','west_east']


class brandAdmin(admin.ModelAdmin):
    list_display = ['name','index']
    search_fields = ['name','index']
    list_filter = ['name','index']

class sizeAdmin(admin.ModelAdmin):
    list_display = ['name','index']
    search_fields = ['name','index']
    list_filter = ['name','index']


class CarAdmin(admin.ModelAdmin):
    list_display = ['goods','sum_price','user']
    search_fields = ['goods','sum_price','user']
    list_filter = ['goods','sum_price','user']

admin.site.register(User)
admin.site.register(Ad)
admin.site.register(Category,categoryAdmin)
admin.site.register(Brand,brandAdmin)
admin.site.register(Size,sizeAdmin)
admin.site.register(Tag)
admin.site.register(Furniture)
admin.site.register(Car, CarAdmin)
admin.site.register(OrderInfo)
admin.site.register(Comment)
