from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

# Create your models here.
class mock_Category(models.Model):
    title=models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural='Category'
    def __str__(self):
        return self.title
    

class mock_Question(models.Model):
    category=models.ForeignKey(mock_Category, on_delete=models.CASCADE) 
    question=models.TextField()
    opt_1=models.CharField(max_length=100)
    opt_2=models.CharField(max_length=100)
    opt_2=models.CharField(max_length=100)
    opt_3=models.CharField(max_length=100)
    opt_4=models.CharField(max_length=100)
    right_opt=models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural='Question'
    
    def __str__(self):
        return self.question  
    
    
    
class User_Submitted(models.Model):
    question=models.ForeignKey(mock_Question, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Submitted_Answer=models.TextField(max_length=100,blank=True,default='null')
    
    
    class Meta:
        verbose_name_plural='User Submitted Answer'
        

class leaderboard(models.Model):
    
    # user=models.ForeignKey(User, on_delete=models.CASCADE)
    user=models.CharField(max_length=100)
    percent=models.FloatField(max_length=100)
    
    class Meta:
        verbose_name_plural='leaderboard'
        
        