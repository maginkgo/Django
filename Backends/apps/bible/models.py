from django.db import models

class Biblia(models.Model):
	version = models.CharField(max_length=50)

	def __unicode__(self):
		return self.version

class Verso(models.Model):
	biblia = models.ForeignKey(Biblia)
	numero = models.IntegerField()
	capitulo = models.IntegerField()
	libro = models.CharField(max_length=20)
	texto = models.TextField()

	def __unicode__(self):
		return u'%s %d : %d' % (self.libro, self.capitulo, self.numero)





