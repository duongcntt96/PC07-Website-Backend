from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=100)
    slogan = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class UserProfile(models.Model):
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, primary_key=True, related_name="profile")
    team = models.ManyToManyField(Team, blank=True, null=True)
    ten = models.CharField(max_length=100)
    ngay_sinh = models.CharField(max_length=10, blank=True, null=True)
    que_quan = models.CharField(max_length=500, blank=True, null=True)
    ho_khau = models.CharField(max_length=500, blank=True, null=True)
    sdt = models.CharField(max_length=10, blank=True, null=True)
    trinh_do_hoc_van = models.CharField(max_length=10, blank=True, null=True)
    trinh_do_chuyen_mon = models.CharField(
        max_length=50, blank=True, null=True)
    cap_bac = models.CharField(max_length=20, blank=True, null=True)
    ngay_vao_nganh = models.CharField(max_length=10, default="1/1/2021")

    def __str__(self):
        return self.ten
