from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
            )
        user.is_admin = True
        user.save(using=self._db)
        return user    

class Usuario(AbstractBaseUser, PermissionsMixin):
    id=models.BigAutoField(primary_key=True)
    rol=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    celular=models.CharField(max_length=50)
    e_mail=models.EmailField(max_length=50)
    direccion=models.CharField( max_length=50)
    username=models.CharField(max_length=50, unique=True)
    password=models.CharField(max_length=256) #La longitud debe ser 256 debido a que se almacena el Hash del password

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
        
    objects = UserManager()
    USERNAME_FIELD = 'username'








    
