from django.contrib import admin
from .models import *

admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Level)

