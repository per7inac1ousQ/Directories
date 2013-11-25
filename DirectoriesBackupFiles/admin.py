from django.contrib import admin
from Directories.models import Attributes
from Directories.models import Department, Instructors, Katefth, KatefthKykloi, Kykloi, KykloiExamina, ModuleKykloi, Modules, ModulesTutors,  PubInstr, PubTypes, Publications, Ranks, Service, Users, Works

class AttribAdmin(admin.ModelAdmin):
	list_display=['descr','descr_en', 'notes']

class DepAdmin(admin.ModelAdmin):
	list_display = ('tmima_per', 'proedros', 'pr_spoudwn', 'pr_spoudwn_en', 'tmima_per_en', 'tmima_en', 'homepage', 'homepage_en', 'lastupdate')

class InstAdmin(admin.ModelAdmin):
	list_display = ('cv', 'cv_en', 'research', 'research_en', 'subject', 'subject_en', 'lastupdate')

class KatAdmin(admin.ModelAdmin):
	list_display = ('perigrafi_kat', 'perigrafi_kat_en')

class KatKyAdmin(admin.ModelAdmin):
	list_display = ('kat_id', 'kyklos_id')

class KyAdmin(admin.ModelAdmin):
	list_display = ('name', 'name_en', 'notes', 'notes_en', 'dept_id', 'examina', 'indexing')

class KyExAdmin(admin.ModelAdmin):
	list_display = ('examina', 'notes', 'notes_en', 'comments')

class ModKyAdmin(admin.ModelAdmin):
	list_display = ('module_id', 'kyklos_id', 'semester', 'indexing')

class ModAdmin(admin.ModelAdmin):
	list_display = ('module', 'description', 'choice', 'module_en', 'description_en', 'notes', 'notes_en')

class ModTutAdmin(admin.ModelAdmin):
	list_display = ('tutor_id', 'last_update')

class PubInstAdmin(admin.ModelAdmin):
	list_display = ('instrid', 'cduom', 'lastupdate')

class PubTypAdmin(admin.ModelAdmin):
	list_display = ('type_description', 'lastupdate')

class PublAdmin(admin.ModelAdmin):
	list_display = ('description', 'year', 'typeid', 'filelink', 'pubdate', 'lastupdate')

class RanksAdmin(admin.ModelAdmin):
	list_display = ('idiotita_per', 'idiotita_per_en', 'notes')

class ServAdmin(admin.ModelAdmin):
	list_display = ('name', 'name_en', 'notes', 'notes_en', 'is_academic')

class UsersAdmin(admin.ModelAdmin):
	list_display = ('username', 'password', 'status')

class WorksAdmin(admin.ModelAdmin):
	list_display = ('service_id', 'attribute_id', 'phone', 'primary_academic', 'lastupdate')

admin.site.register(Attributes, AttribAdmin)
admin.site.register(Department, DepAdmin)
admin.site.register(Instructors, InstAdmin)
admin.site.register(Katefth, KatAdmin)
admin.site.register(KatefthKykloi, KatKyAdmin)
admin.site.register(Kykloi, KyAdmin)
admin.site.register(KykloiExamina, KyExAdmin)
admin.site.register(ModuleKykloi, ModKyAdmin)
admin.site.register(Modules, ModAdmin)
admin.site.register(ModulesTutors, ModTutAdmin)
admin.site.register(PubInstr, PubInstAdmin)
admin.site.register(PubTypes, PubTypAdmin)
admin.site.register(Publications, PublAdmin)
admin.site.register(Ranks, RanksAdmin)
admin.site.register(Service, ServAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Works, WorksAdmin)



