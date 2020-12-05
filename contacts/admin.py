from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','city','created_date')
    list_display_links=('id','first_name','last_name','email')
    search_fields=('first_name','city','car_title','state')
    list_per_page=25

admin.site.register(Contact,ContactAdmin)
