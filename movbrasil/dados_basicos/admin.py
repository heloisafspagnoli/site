from django.contrib import admin
from models import quem_somos_model, equipe_model
from cursos.models import  local_model, curso_model, palestrantes_model, programacao_model

admin.site.register(quem_somos_model)
admin.site.register(equipe_model)
admin.site.register(local_model)
admin.site.register(curso_model)
admin.site.register(palestrantes_model)
admin.site.register(programacao_model)
