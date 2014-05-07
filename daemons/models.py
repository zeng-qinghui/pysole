#encoding=utf-8
from django.db import models

# Create your models here.
class Daemon(models.Model):
    id = models.AutoField(primary_key=True)
    display_name = models.CharField("名称", max_length=256, unique=True)
    script_name = models.CharField("脚本路径", max_length=256)
    running_status = models.SmallIntegerField(
        "状态", choices=[(-1, 'STOP'), (0, 'UNKNOWN'), (1, 'RUNNING'), (2, 'WAITING')]
    )
    last_update_time = models.DateTimeField("最后更新时间", auto_now=True)

    class Meta:
        verbose_name = '守护脚本'
        verbose_name_plural = '守护脚本'

    def __unicode__(self):
        return self.display_name

    def natural_key(self):
        return self.display_name

class Cron(models.Model):
    id = models.AutoField(primary_key=True)
    display_name = models.CharField("名称", max_length=256, unique=True)
    script_name = models.CharField("脚本路径", max_length=256)
    last_started_time = models.DateTimeField("最后开始时间", auto_now=True)
    last_finished_time = models.DateTimeField("最后结束时间", auto_now=True)
    log = models.TextField("最后运行日志")

    class Meta:
        verbose_name = '定时脚本'
        verbose_name_plural = '定时脚本'

    def __unicode__(self):
        return self.display_name

    def natural_key(self):
        return self.display_name