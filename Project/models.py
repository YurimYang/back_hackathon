from django.db import models
from django.contrib.auth.models import User
#from Field.models import Field_1, Field_2, Field_3

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=45)  

class Club(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE, db_column= "user_id") #user가 사라지면 그 user의 동아리도 사라지도록 하는게 좋을까요..? protect로 해두면 동아리는 사라지지않습니다. 일단 cascade로 해둘게요!
    title = models.CharField(max_length=60)
    type = models.IntegerField() #0이면 교내활동, 1이면 대외활동
    leader = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length= 45)
    body = models.CharField(max_length=1000)
    #field1_id = models.ForeignKey(Field_1, on_delete = models.PROTECT, db_column="field1_id")
    #field2_id = models.ForeignKey(Field_2, on_delete = models.PROTECT, db_column="field2_id")
    #field3_id = models.ForeignKey(Field_3, on_delete = models.PROTECT, db_column="field3_id")
    #school_id = models.ForeignKey(School, on_delete= models.CASCADE, db_column="school_id")
    #def __str__(self):
        #return self.title

class Matching(models.Model):
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE, db_column="club_id")
    match_date = models.DateTimeField()
    match_body = models.CharField(max_length=1000)
