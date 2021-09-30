from django.db import models

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField(max_length=200)

    def __str__(self):
        return self.question_text

