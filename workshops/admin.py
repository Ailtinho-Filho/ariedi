from django.contrib import admin

from workshops.models import Workshop, WorkshopImage


class WorkshopImageInline(admin.TabularInline):
    model = WorkshopImage
    extra = 2


class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'active')

    inlines = [
        WorkshopImageInline,
    ]


admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(WorkshopImage)
