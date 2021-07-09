from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_id_id = models.CharField(max_length = 45) #사용자 id
    user_password = models.CharField(max_length = 45) #사용자 pw
    user_name = models.CharField(max_length = 15) #사용자 성함 
    user_leader = models.IntegerField() #0이면 리더 1이면 리더 X

    def __str__(self):
        return self.user_id_id
