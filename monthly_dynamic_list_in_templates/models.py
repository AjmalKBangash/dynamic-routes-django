from typing import Type
from django.db import models
from django.db.models.options import Options


# Create your models here.
class monthsurlhistory(models.Model):
    urlhistory = models.CharField( max_length=150)
    
    def __str__(self):
        return self.urlhistory
    
    class Meta:
        # db_table = 'Months_Historyyyy'
        verbose_name = 'Months_History'









# class clicking_history():
#     def __init__(self):
#         self.varr = 'ok'
#         print("Salamoooooonammmm")
#         print(self.varr)
#     def funai(self):    
#         print("salammmm")


# obj1 = clicking_history()
# obj1.funai()
# print("w.Salammmmmmm")
# print(obj1.varr)


