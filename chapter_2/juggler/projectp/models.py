from django.db import models


class Project(models.Model):
    """A project for manage"""
    name = models.CharField(max_length=50,
                            help_text="The name of the Project.")

    def __str__(self):
        return self.name


class Task(models.Model):
    """A project task"""
    name = models.CharField(max_length=50,
                            help_text="The name of the Task")
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.name
