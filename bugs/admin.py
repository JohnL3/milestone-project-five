from django.contrib import admin
from .models import Bug, BugComment,BugVotes


admin.site.register(Bug)
admin.site.register(BugComment)
admin.site.register(BugVotes)
