from django.db import models

# Create your models here.
class Question(models.Model):
    
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')
    
class Choice(models.Model):
    
    question = models.ForeignKey(Question, models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
def __str__(self):
    return f"{Question.question_text}, {Choice.choice_text}"