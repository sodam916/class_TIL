from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # 정참조 이름 = 매니필드 & 방향성 정보(True : 방향성 있음/ Flase : 방향성 없음) & 역참조 이름
