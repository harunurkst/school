from django.db import models

class Batch(models.Model):
    name = models.CharField(max_length=50)
    member = models.IntegerField()

    def __str__(self):
        return str(self.name)

class Profile(models.Model):
    photo = models.ImageField()
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.address

class StudentManager(models.Manager):
    def adults(self):
        std_list = StudentInfo.objects.filter(age__gte=18)
        return std_list


class StudentInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender_ls = (('m', 'Male'), ('f', 'Female'))
    gender = models.CharField(max_length=10, choices=gender_ls)
    fathers_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    mobile_nember = models.IntegerField()
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, blank=True, null=True)
    profile = models.OneToOneField(Profile, on_delete=models.SET_NULL, blank=True, null=True)

    objects = StudentManager()
    
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def __str__(self):
        return self.first_name