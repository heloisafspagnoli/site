from django.contrib import admin

from models import chamada_model, parceiros_model, quem_somos_model, equipe_model, endereco_contato_model, local_model, curso_model, palestrantes_model, programacao_model

admin.site.register(chamada_model)
admin.site.register(quem_somos_model)
admin.site.register(equipe_model)
admin.site.register(parceiros_model)
admin.site.register(endereco_contato_model)
admin.site.register(local_model)
admin.site.register(curso_model)
admin.site.register(palestrantes_model)
admin.site.register(programacao_model)