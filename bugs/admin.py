from django.contrib import admin
from .models import Bug, BugComment


admin.site.register(Bug)
admin.site.register(BugComment)
