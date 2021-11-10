from django.contrib import admin
from .models import Comments, Reply

# Register your models here.
@admin.register(Comments,Reply)
class DefaultAdmin(admin.ModelAdmin):
    pass



# admin.site.register(Comments)
# admin.site.register(Reply)
