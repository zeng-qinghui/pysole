#encoding=utf-8
from django.db import models


# Create your models here.
class Daemon(models.Model):
    id = models.AutoField(primary_key=True)
    display_name = models.CharField("Display Name", max_length=256, unique=True)
    script_path = models.CharField("Script Path", max_length=256)
    auto_restart = models.BooleanField("Auto Restart")
    last_restart_time = models.DateTimeField("Last Restart Time", null=True)
    running_status = models.SmallIntegerField(
        "Status", choices=[(-1, 'STOP'), (0, 'UNKNOWN'), (1, 'RUNNING'), (2, 'STARTING'), (3, 'PLANING')], default=0
    )
    last_update_time = models.DateTimeField("Last Update", null = True)

    class Meta:
        verbose_name = 'Daemon Script'
        verbose_name_plural = 'Daemon Scripts'

    def __unicode__(self):
        return self.display_name

    def natural_key(self):
        return self.display_name


class Cron(models.Model):
    id = models.AutoField(primary_key=True)
    display_name = models.CharField("Display Name", max_length=256, unique=True)
    script_path = models.CharField("Script Path", max_length=256)
    run_time = models.CharField("Time Config", max_length=32)
    last_started_time = models.DateTimeField("Last Started Time", null=True)
    last_finished_time = models.DateTimeField("Last Finished Time", null=True)
    log = models.TextField("Last Log")

    class Meta:
        verbose_name = 'Cron Script'
        verbose_name_plural = 'Cron Script'

    def __unicode__(self):
        return self.display_name

    def natural_key(self):
        return self.display_name