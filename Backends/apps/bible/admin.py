from django.contrib import admin

from .models import Biblia
from .models import Verso


admin.site.register(Biblia)
admin.site.register(Verso)
