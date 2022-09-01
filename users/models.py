from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, email, nickname, name, birth_year, birth_month, birth_day, gender, password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError('must have user email')
        if not nickname:
            raise ValueError('must have user nickname')
        if not name:
            raise ValueError('must have user name')
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
            name = name,
            birth_year = birth_year,
            birth_month=birth_month,
            birth_day=birth_day,
            gender = gender,
        )
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # 관리자 user 생성
    def create_superuser(self, email, nickname, name, birth_year, birth_month, birth_day, gender, password=None):
        user = self.create_user(
            email,
            password = password,
            nickname = nickname,
            name = name,
            birth_year = birth_year,
            birth_month=birth_month,
            birth_day=birth_day,
            gender = gender,
            is_staff=True,
            is_admin=True,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False)
    birth_year = models.IntegerField(default=0, null=False, blank=False)
    birth_month = models.IntegerField(default=0, null=False, blank=False)
    birth_day = models.IntegerField(default=0, null=False, blank=False)
    gender = models.CharField(default='',max_length=10, null=False, blank=False)

    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = 'nickname'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['email', 'name', 'birth_year', 'birth_month', 'birth_day', 'gender']

    def __str__(self):
        return self.nickname

    @property
    def is_staff(self):
        return self.is_admin
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
        
    def has_module_perms(self, app_label):
        return self.is_admin