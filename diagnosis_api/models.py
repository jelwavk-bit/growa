from django.db import models

class DiseaseInfo(models.Model):
    label = models.CharField(max_length=100, unique=True) # THIS must match the names above
    display_name = models.CharField(max_length=200)
    description = models.TextField()
    symptoms = models.TextField()
    causes = models.TextField()
    preventive_measures = models.TextField()
    solutions = models.TextField()

    def __str__(self):
        return self.display_name