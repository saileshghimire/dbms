from django.db import models

# Create your models here.
Gender_choices = (('male','male'),('female','female'),('other','other'))
Admission_fees = (('Reguar','Regular'),('FullFee','Fullfee'))


class StudentDetail(models.Model):
    firstname = models.CharField(max_length=15, blank=False)
    middlename = models.CharField(max_length=15,blank=True)
    lastname = models.CharField(max_length=15, blank=False)
    Gender = models.CharField(max_length=7,choices=Gender_choices,blank=False,default='male')
    rollnumber = models.CharField(max_length=15, blank=False)
    phonenumber = models.CharField(max_length=20,blank=False)
    DateofBirth = models.CharField(max_length=12,blank=False)
    email = models.CharField(max_length=50,blank=False)
    fathername = models.CharField(max_length=25,blank=False)
    mothername = models.CharField(max_length=25,blank=False)
    DateofAdmission = models.CharField(max_length=12,blank=False)
    Fees = models.CharField(max_length=10,choices=Admission_fees,blank=False,default='FullFees')
    
    def __str__(self):
        return self.firstname + " " +self.middlename + " " + self.lastname
    
