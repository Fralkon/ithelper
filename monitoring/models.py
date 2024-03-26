from django.db import models

class User(models.Model) : 
    id = models.AutoField(primary_key = True)
    login = models.TextField(unique=True)
    id_chat = models.BigIntegerField(unique=True)
    branchs = models.TextField()
    name = models.CharField(max_length = 30)
    col_sq = models.IntegerField()
    monitoring = models.BooleanField()
    def __str__(self):
        return self.name

class Info(models.Model):
    id = models.AutoField(primary_key = True)
    type = models.CharField(max_length = 10)
    topic = models.CharField(max_length = 20)
    info = models.TextField()
    file = models.CharField(max_length = 60)
    def __str__(self):
        return self.type + ' ' + self.topic

class Equipment_type(models.Model):
    id = models.AutoField(primary_key = True)
    type = models.CharField(max_length = 20)
    def __str__(self):
        return self.type

class Branch(models.Model):    
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 6,unique=True)
    adress = models.CharField(max_length = 60)    
    def __str__(self):
        return self.name

class Equipment(models.Model):
    id = models.AutoField(primary_key = True)
    branch = models.ForeignKey(Branch, on_delete = models.CASCADE)    
    name = models.CharField(max_length = 20)
    ip = models.CharField(max_length = 15,unique=True)
    type = models.ForeignKey(Equipment_type, on_delete = models.CASCADE)
    status = models.BooleanField()
    monitoring = models.BooleanField()
    time_off = models.DateTimeField()    
    def __str__(self):
        return self.name

class ServiceOrganization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True)
    contact = models.TextField()
    def __str__(self):
        return self.name

class Task(models.Model):
    id = models.AutoField(primary_key= True)
    branch = models.ForeignKey(Branch, on_delete = models.CASCADE)
    task = models.TextField()
    type = models.IntegerField()
    status = models.BooleanField()
    organization = models.ForeignKey(ServiceOrganization, on_delete = models.CASCADE)
    comment = models.TextField()    
    def __str__(self):
        return self.task

class PrinterModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True)
    driver = models.TextField()
    def __str__(self):
        return self.name
    
class Printer(models.Model):
    id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete = models.CASCADE)
    name = models.TextField()
    model = models.ForeignKey(PrinterModel, on_delete = models.CASCADE)
    ip = models.TextField()
    def __str__(self):
        return self.branch.name + self.name