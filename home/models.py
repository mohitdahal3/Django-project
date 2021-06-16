from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50 , default = '')
    email = models.CharField(max_length = 80 , default = '')
    phone = models.CharField(max_length = 20 , default= '')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True , blank=True)

    def __str__(self):
        if(len(self.message) > 10):
            return (f"Message from {self.name} - {self.message[:10]}...")
        else:    
            return (f"Message from {self.name} - {self.message[:10]}")
            