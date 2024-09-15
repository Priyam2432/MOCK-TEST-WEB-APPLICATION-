from django.contrib import admin
from. import models
# Register your models here.
admin.site.register(models.mock_Category)
admin.site.register(models.mock_Question)

class User_Submittedadmin(admin.ModelAdmin):
    list_display=['question','user','Submitted_Answer']
    
admin.site.register(models.User_Submitted,User_Submittedadmin)

class leaderboardadmin(admin.ModelAdmin):
    list_display=['user','percent'] 
admin.site.register(models.leaderboard,leaderboardadmin)