#encoding=utf-8
from django.contrib import admin
from daemons import models
from datetime import datetime

class DaemonAdmin(admin.ModelAdmin):
    list_display = ["display_name", "script_path", "running_status", "last_update_time","auto_restart","last_restart_time"]
    list_filter = ["running_status", "last_update_time","auto_restart"]
    readonly_fields = ["running_status", "last_update_time","last_restart_time"]

    def restart_daemon_script(self, request, queryset):
        short_description = "Restart Selected scripts"
        queryset.update(running_status=3)
        self.message_user(request, "Daemon will restart soon")

    actions=[restart_daemon_script]


class CronAdmin(admin.ModelAdmin):
    list_display = ["display_name", "script_path","run_time", "last_started_time", "last_finished_time","log"]
    list_display_links = ["display_name","log"]
    readonly_fields = ["last_started_time", "last_finished_time","log"]

admin.site.register(models.Daemon ,DaemonAdmin)
admin.site.register(models.Cron,CronAdmin)