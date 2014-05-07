#encoding=utf-8
from django.contrib import admin
from daemons import models

class DaemonAdmin(admin.ModelAdmin):
    list_display = ["display_name", "script_name", "running_status", "last_update_time"]
    list_filter = ["running_status", "last_update_time"]
    readonly_fields = ["running_status", "last_update_time"]

class CronAdmin(admin.ModelAdmin):
    list_display = ["display_name", "script_name", "last_started_time", "last_finished_time","log"]
    list_display_links = ["log"]
    readonly_fields = ["last_started_time", "last_finished_time"]

admin.site.register(models.Daemon ,DaemonAdmin)
admin.site.register(models.Cron,CronAdmin)