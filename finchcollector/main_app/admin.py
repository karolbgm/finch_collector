from django.contrib import admin
from .models import Bird, Feeding

# Register your models here.
admin.site.register(Bird)
# register the new Feeding Model
admin.site.register(Feeding)