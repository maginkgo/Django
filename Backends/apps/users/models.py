from django.db import models

# Importar clase para crear nuestro modelo de usuario
from django.contrib.auth.models import AbstractBaseUser
# Importar clase para crear el administrador del modelo
from django.contrib.auth.models import BaseUserManager
# Importar clase para dar permisos a los usuarios
from django.contrib.auth.models import PermissionsMixin

#Creamos el Administrador del modelo User:
class UserManager(BaseUserManager):

	def _create_user(self,username,email,password,is_staff,is_superuser,**extra_fields):
		#if not email: # Preguntamos si viene un email
		#	raise ValueError('El email es obligatorio') #Mostrar mensaje de error si no hay email
		email=self.normalize_email(email) #Poner todo en minusculas

		#Creamos el usuario:
		user=self.model(username=username,email=email,is_active=True,is_staff=is_staff,is_superuser=is_superuser,
							**extra_fields)

		#Seteamos el password:
		user.set_password(password)

		#Guardamos el user en la base por defecto:
		user.save(using=self._db)

		return user 

	#Metodo para crear un usuario normal:
	def create_user(self, username,email,password=None,**extra_fields):
		return self._create_user(username,email,password,False,False,**extra_fields)

	#Metodo para crear un superusuario
	def create_superuser(self,username,email,password,**extra_fields):
		return self._create_user(username,email,password,True,True,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):

	username = models.CharField(max_length=50, unique=True)
	email = models.EmailField(max_length=50, unique=False)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	avatar = models.URLField()
	status = models.BooleanField(default=False)

	#Atributo intermediario entre las transacciones de cada modelo. 
	#El 'manager' de este modelo:
	objects = UserManager()

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def get_short_name(self):
		return self.username