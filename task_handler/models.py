from django.db import models
from signup_handler.models import User

class task(models.Model):
    priority_chocies = [
        ('Urgent', (
            ('Urgent & Important', 'Urgent & Important'),
            ('Urgent & Not Important', 'Urgent & Not Important')
            )),
        ('Not Urgent', (
            ('Not Urgent & Important', 'Not Urgent & Important'),
            ('Not Urgent & Not Important', 'Not Urgent & Not Important')
            ))
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length = 100,choices = priority_chocies, default = '1')
    title = models.CharField(max_length = 100)
    description = models.TextField()
    complete = models.BooleanField(default = False)
    create = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create']