from django.db import models

class ShowManager(models.Manager):
    def test_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title name should be at least 2 charaters"
        if postData['release_date'] == "":
            errors["release_date"] = "Please enter a release date"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['description']) == 0:
            return errors
        if len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    network = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"<Show object: {self.id} {self.title} {self.release_date} {self.network} {self.description}"

