from django.contrib import admin

from .models import User, Immobilier, Agence, Demande, Offre, Besoins, Ville, Types


admin.site.register(User)
admin.site.register(Immobilier)
admin.site.register(Agence)
admin.site.register(Demande)
admin.site.register(Offre)
admin.site.register(Besoins)
admin.site.register(Ville)
admin.site.register(Types)

