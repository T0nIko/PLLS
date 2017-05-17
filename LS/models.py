from django.db import models


class Code(models.Model):
    text = models.TextField()
    task_name = models.TextField()
    c_answer = models.TextField()

    def __str__(self):
        return "Task name: {0}\nText: {1}\nCorrect answer: {2}".format(self.task_name, self.text, self.c_answer)
