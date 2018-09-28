from django.contrib import admin
from .models import * #StudentInfo, Batch, Profile


admin.site.register(StudentInfo)
admin.site.register(Batch)
admin.site.register(Profile)