from django.contrib import admin

from models import chamada_model, parceiros_model, quem_somos_model,\
                   equipe_model, endereco_contato_model, local_model,\
                   curso_model, palestrantes_model, programacao_model,\
                   material_incluso_model, img_qms_model


class CursoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}


admin.site.register(chamada_model)
admin.site.register(parceiros_model)
admin.site.register(quem_somos_model)
admin.site.register(equipe_model)
admin.site.register(endereco_contato_model)
admin.site.register(local_model)
admin.site.register(curso_model, CursoAdmin)
admin.site.register(palestrantes_model)
admin.site.register(programacao_model)
admin.site.register(material_incluso_model)
admin.site.register(img_qms_model)
