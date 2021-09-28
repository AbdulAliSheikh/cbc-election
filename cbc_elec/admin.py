import csv

from django.contrib import admin

# Register your models here.
from django.http import HttpResponse

from .models import *


def download_csv(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response


class VoterAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'cnic', 'address', 'gender', 'phase', 'created_at', 'updated_at')
    search_fields = ('address', 'phase')
    list_filter = ['gender', 'created_at']
    actions = [download_csv]


admin.site.site_header = "CBC Election Admin"
admin.site.site_title = "CBC Election Admin Portal"
admin.site.index_title = "Welcome to CBC Election Portal"
admin.site.register(Voter, VoterAdmin)

# csv export data
