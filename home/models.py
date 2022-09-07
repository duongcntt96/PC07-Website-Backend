from django.db import models
# Create your models here.

class feedBack(models.Model):
	body = models.TextField()
	create_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.body

class Post(models.Model):
	title = models.CharField(max_length=500)
	body = models.TextField()
	create_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title

class Chu_de(models.Model):
	chu_de = models.CharField(max_length=500)
	thoi_gian_tao = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.chu_de

class Bai_viet(models.Model):
	chu_de = models.ForeignKey(Chu_de, on_delete=models.RESTRICT)
	tieu_de = models.CharField(max_length=500)
	noi_dung = models.TextField()
	file_dinh_kem = models.FileField(default="")
	thoi_gian_tao = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.tieu_de