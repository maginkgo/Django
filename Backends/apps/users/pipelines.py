#Modificamos el flujo de la logica que hace Python Social Auth de la autentificacion
"""
El "pipeline" es un mecanismo extendible donde podemos agregar funciones propias 
a realizar durante la autentificacion
"""
#Funcion para traer el avatar del user
'''
Parametros:
>backend: Nos dice desde donde nos logueamos, facebook, o twitter o google+
>strategy: 
>details: Retorna Username, Nombre y Apellido del user
>response: Retorna toda la info de perfil de la red social 
>user:objeto del usuario que se esta logueando 
'''
def get_avatar(backend, strategy, details, response, user=None, *args, **kwargs):
	url=None
	if backend.name == 'facebook':
		url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
	if backend.name == 'twitter':
		url = response.get('profile_image_url', '').replace('_normal', '')

	if url:
		user.avatar = url
		user.save()


