from django.db import models
from datetime import date
from django.utils import timezone
class Group(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=200)
    cost = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name
    

class Students(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    pay = models.PositiveIntegerField()
    added_day = models.DateField(default=date.today)
    dedline = models.DateField()
    # @property
    # def status(self):
    #     if self.added_day >= self.dedline:
    #         return "✅ Active"
    #     elif self.added_day <= self.dedline:
    #         return "❌ Inactive"
    
    @property
    def status(self):
        hozirgi_kun = timezone.now().date()
        if self.added_day <= hozirgi_kun <= self.dedline:
            return "✅ Active"
        else:
            return "❌ Inactive"
        
    def __str__(self):
        return f"{self.name} | {self.status}"
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'