from django.contrib import admin

<<<<<<< HEAD
# Register your models here.
=======
from .models import Db
from .models import Rubric


class DbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Db, DbAdmin)
admin.site.register(Rubric)

>>>>>>> 07.02.2021