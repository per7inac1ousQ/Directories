# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
from django.db import models

class Attributes(models.Model):
    attr_id = models.AutoField(primary_key=True)
    descr = models.CharField(max_length=140)
    descr_en = models.CharField(max_length=140)
    notes = models.CharField(max_length=250, blank=True)
    class Meta:
        db_table = 'attributes'
	verbose_name= 'Attributes'
# maybe instantiate a def _unicode_ function that will return model's name?

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    tmima_per = models.TextField()
    proedros = models.IntegerField(default='0')
    pr_spoudwn = models.TextField()
    pr_spoudwn_en = models.TextField()
    tmima_per_en = models.TextField()
    tmima_en = models.CharField(max_length=5)
    homepage = models.TextField()
    homepage_en = models.TextField()
    lastupdate = models.DateTimeField()
    class Meta:
        db_table = 'department'
	verbose_name= 'Department'

class Instructors(models.Model):
    instr_id = models.AutoField(primary_key=True, default='0')
    cv = models.TextField(blank=True)
    cv_en = models.TextField(blank=True)
    research = models.TextField(blank=True)
    research_en = models.TextField(blank=True)
    subject = models.CharField(max_length=255, blank=True)
    subject_en = models.CharField(max_length=255, blank=True)
    lastupdate = models.DateTimeField()
    class Meta:
        db_table = 'instructors'
	verbose_name= 'Instructors'

class Katefth(models.Model):
    kat_id = models.AutoField(primary_key=True)
    perigrafi_kat = models.CharField(max_length=100)
    perigrafi_kat_en = models.CharField(max_length=100)
    class Meta:
        db_table = 'katefth'
	verbose_name= 'Katefthnsh'

class KatefthKykloi(models.Model):
    kat_id = models.IntegerField(primary_key=True)
    kyklos_id = models.IntegerField()
    class Meta:
        db_table = 'katefth_kykloi'
	unique_together = ("kat_id", "kyklos_id")
	verbose_name= 'Katefthnsh kykloi'

class Kykloi(models.Model):
    kyklos_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    notes_en = models.TextField(blank=True)
    dept_id = models.IntegerField(blank=True, null=True)
    examina = models.IntegerField()
    indexing = models.IntegerField(default='0000')
    class Meta:
        db_table = 'kykloi'
	verbose_name= 'Kykloi'

class KykloiExamina(models.Model):
    id = models.AutoField(primary_key=True)
    examina = models.TextField()
    notes = models.CharField(max_length=255, blank=True)
    notes_en = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)
    class Meta:
        db_table = 'kykloi_examina'
	verbose_name= 'Kykloi examina'

class ModuleKykloi(models.Model):
    module_id = models.IntegerField(primary_key=True, default='0')
    kyklos_id = models.IntegerField(default='0')
    semester = models.IntegerField(default='0')
    indexing = models.IntegerField(default='99')
    class Meta:
        db_table = 'module_kykloi'
	unique_together = (("module_id", "kyklos_id", "semester"),)
	verbose_name= 'Modules Kyklwn'

class Modules(models.Model):
    id = models.AutoField(primary_key=True)
    module = models.CharField(max_length=255, default='')
    description = models.TextField()
    choice = models.IntegerField(default='0')
    module_en = models.CharField(max_length=255, default='')
    description_en = models.TextField()
    notes = models.CharField(max_length=255, default='')
    notes_en = models.CharField(max_length=255)
    class Meta:
        db_table = 'modules'
	verbose_name= 'Modules'

class ModulesTutors(models.Model):
    module_id = models.IntegerField(primary_key=True, default='0')
    tutor_id = models.IntegerField(default='0')
    last_update = models.DateTimeField()
    class Meta:
        db_table = 'modules_tutors'
	unique_together = (("module_id", "tutor_id"),)
	verbose_name= 'Modules tutors'

class PubInstr(models.Model):
    pubid = models.IntegerField(primary_key=True, default='0')
    instrid = models.IntegerField(default='0')
    cduom = models.IntegerField(default='1')
    lastupdate = models.DateTimeField()
    class Meta:
        db_table = 'pub_instr'
	unique_together = (("pubid", "instrid"),)
	verbose_name= 'Publication instr'

class PubTypes(models.Model):
    id = models.AutoField(primary_key=True, default='0')
    type_description = models.CharField(max_length=255)
    lastupdate = models.DateTimeField()
    class Meta:
        db_table = 'pub_types'
	verbose_name= 'Publication types'

class Publications(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    year = models.CharField(max_length=4, default='')
    typeid = models.IntegerField(default='0')
    filelink = models.CharField(max_length=255, blank=True)
    pubdate = models.DateField(blank=True, null=True)
    lastupdate = models.DateTimeField()
    class Meta:
        db_table = 'publications'
	verbose_name= 'Publications'

class Ranks(models.Model):
    rank_id = models.AutoField(primary_key=True)
    idiotita_per = models.CharField(max_length=150, default='')
    idiotita_per_en = models.CharField(max_length=150, default='')
    notes = models.CharField(max_length=250, blank=True)
    class Meta:
        db_table = 'ranks'
	verbose_name= 'Ranks'

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    name_en = models.CharField(max_length=150, blank=True)
    notes = models.TextField(blank=True)
    notes_en = models.TextField(blank=True)
    is_academic = models.IntegerField(default='0')
    class Meta:
        db_table = 'service'
	verbose_name= 'Service'

class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=20, default='')
    password = models.CharField(max_length=4, default='ldap')
    status = models.IntegerField(default='1')
    class Meta:
        db_table = 'users'
	verbose_name= 'Users'

class Works(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    service_id = models.IntegerField()
    attribute_id = models.IntegerField(default='44')
    phone = models.CharField(max_length=36, blank=True)
    primary_academic = models.IntegerField()
    lastupdate = models.DateTimeField()
    class Meta:
        db_table = 'works'
	unique_together = (("emp_id", "service_id", "attribute_id"),)
	verbose_name= 'Works'

