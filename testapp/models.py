from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Credentials(models.Model):
    name = models.CharField(max_length=30)
    data = models.TextField()
    
    def __unicode__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=50)
    subject_id = models.CharField(max_length=20, unique=True)
    syllabus = models.TextField()
    
    def __unicode__(self):
        return self.name
        
class Assignment(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=0)
    assignment_id = models.CharField(max_length=30, unique=True)
    drive_file_id = models.CharField(max_length=100)
    
    
    def __unicode__(self):
        return self.name


class Notes(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=0)
    note_id = models.CharField(max_length=30, unique=True)
    drive_file_id = models.CharField(max_length=100)
    
    
    def __unicode__(self):
        return self.name
    

    
    