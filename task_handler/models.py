from django.db import models
from signup_handler.models import User

class task(models.Model):
    priority_chocies = [
        ('Urgent', (
            (1, 'Urgent & Important'),
            (2, 'Urgent & Not Important')
            )),
        ('Not Urgent', (
            (3, 'Not Urgent & Important'),
            (4,'Not Urgent & Not Important' )
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
        ordering = ['priority']

    def get_tuples(_id = -1, _user = None):
        if _id != -1:
            return task.objects.get(id = _id)
        if _user != None:
            return task.objects.filter(user = _user).values()