from django.db import models

# Create your models here.
class resumedata(models.Model):
    name = models.CharField(max_length=20000)
    phno = models.CharField(max_length=1000)
    address = models.CharField(max_length=7000)
    college = models.CharField(max_length=4000)
    cgpa = models.CharField(max_length=2000)
    comname = models.CharField(max_length=40000)
    brief = models.CharField(max_length=200000)
    start = models.CharField(max_length=4000)
    end = models.CharField(max_length=4000)
    

    

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk}) 

