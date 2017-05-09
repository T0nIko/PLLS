from django.db import models


class Code(models.Model):
    text = models.TextField()
    task_name = models.TextField()
    c_answer = models.TextField()

