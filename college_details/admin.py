from django.contrib import admin
import csv
from django.http import HttpResponse
from .models import  IndianStates,UserProfile2,IndiaCities

def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
        
    writer = csv.writer(response)
    fields = [field.name for field in modeladmin.model._meta.fields]

    writer.writerow(fields)

    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in fields])
    
    return response

export_as_csv.short_description = "Export selected objects as CSV"

class UserProfiles2(admin.ModelAdmin):
    list_display =['id','name','email','phone','date_of_birth','city','state','course','created_at','updated_at','is_active']
    actions = [export_as_csv]


admin.site.register(UserProfile2, UserProfiles2)
admin.site.register(IndianStates)
admin.site.register(IndiaCities)
