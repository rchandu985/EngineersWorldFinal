from django.db import models

# Create your models here.

class Years(models.Model):
    name=models.CharField(max_length=1000,default='',blank=False)
    """def save(self, *args, **kwargs):
        # Add a fixed value (e.g., 10) to all fields before saving
        self.name=self.name.title()
        
        super(Years, self).save(*args, **kwargs)"""

    def __str__(self):
        return self.name
class Sems(models.Model):
    name=models.CharField(max_length=1000,default='',blank=False)
    """def save(self, *args, **kwargs):
        # Add a fixed value (e.g., 10) to all fields before saving
        self.name=self.name.title()
        
        super(Sems, self).save(*args, **kwargs)"""

    def __str__(self):
        return self.name

class Branches(models.Model):
    name=models.CharField(max_length=1000,default="",blank=False)
    def save(self, *args, **kwargs):
        # Add a fixed value (e.g., 10) to all fields before saving
        self.name=self.name.upper()
        
        super(Branches, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Qualifications(models.Model):
    name=models.CharField(max_length=1000,default="",blank=False)
    label=models.CharField(max_length=1000,default="",blank=True)
    value=models.CharField(max_length=1000,default="",blank=True)
    branches = models.ManyToManyField("Branches",related_name="branch")
    year=models.ManyToManyField("Years",related_name="year")
    sem=models.ManyToManyField("Sems", related_name="sem")
    def save(self, *args, **kwargs):
        # Add a fixed value (e.g., 10) to all fields before saving
        self.name=self.name.title()
        self.label = self.name
        self.value = self.name
        super(Qualifications, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name