from django.db import models
from django.db.models.deletion import ProtectedError

# Create your models here.
class Field_1(models.Model):
    field1 = models.CharField(max_length=100)
    #def __str__(self):
        #return self.field1

class Field_2(models.Model):
    #field1_id = models.ForeignKey(Field_1, on_delete=models.PROTECT, db_column="field1_id")
    field2 = models.CharField(max_length=100) 
    #def __str__(self):
        #return self.field1_id.field1 + "/" + self.field2 # 인문/미디어 

class Field_3(models.Model):
    #field1_id = models.ForeignKey(Field_1, on_delete=models.PROTECT, db_column="field_id")
    #field2_id = models.ForeignKey(Field_2, on_delete=models.PROTECT, db_column="field_id_2")
    field3 = models.CharField(max_length=100)
    #def __str__(self):
        #return self.field3 # 인문/미디어/광고 