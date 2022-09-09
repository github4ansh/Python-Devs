from django.db import models


class Employee(models.Model):
    """
    Employee model
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    email_id = models.EmailField(max_length=254, primary_key=True)

    def __str__(self):
        return f'Employee object: {self.first_name} {self.last_name}'

    class Meta:
        db_table = 'employee'
