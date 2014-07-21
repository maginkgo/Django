from django.db import models

class Farmacia(models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	telefono = models.IntegerField(max_length=30)

	def __unicode__(self):
		return self.nombre


class Turno(models.Model):
	fecha = models.DateField()
	farmacia = models.ForeignKey(Farmacia)
	TURNO_24HS = 'a'
	TURNO_PARCIAL = 'b'
	GUARDIA = (
		(TURNO_24HS, '24hs'),
		(TURNO_PARCIAL, 'De 8:30am a 10:00pm'),
		)
	tipo = models.CharField(max_length=1, choices=GUARDIA, default=TURNO_24HS)

	def __unicode__(self):
		return str(self.fecha) 		