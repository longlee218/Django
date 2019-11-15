from django.db import models


class Demo(models.Model):
    name = models.CharField(max_length=35)
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=35)
    birthday = models.DateTimeField(null=True)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)