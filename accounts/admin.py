from django.contrib import admin
from .models import User 

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_number', 'first_name', 'last_name',) # columns in list view
    list_filter = ('id', 'first_name',)  #filter sidebar
    search_fields = ('first_name', 'id', 'email',)  #search bar
   # ordering = ('price',)  #default ordering
   
admin.site.register(User, UserAdmin)

