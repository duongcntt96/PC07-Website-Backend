from django.db import models

# Create your models here.


class Doc(models.Model):

    name = models.CharField(max_length=100)
    text = models.CharField(max_length=500, null=True, blank=True)
    file = models.FileField(upload_to="static")
    date = models.DateField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name + ", " + str(self.date) + ", " + self.text


class Comment(models.Model):
    doc = models.ForeignKey(Doc, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    file = models.FileField(upload_to="static", null=True, blank=True)

    def __str__(self):
        return self.text + '\n' + self.doc.name
