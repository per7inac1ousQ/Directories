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
    attr_id = models.IntegerField(primary_key=True)
    descr = models.CharField(max_length=140)
    descr_en = models.CharField(max_length=140)
    notes = models.CharField(max_length=250, blank=True)
    class Meta:
        managed = False
        db_table = 'attributes'

class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    tmima_per = models.TextField()
    proedros = models.IntegerField()
    pr_spoudwn = models.TextField()
    pr_spoudwn_en = models.TextField()
    tmima_per_en = models.TextField()
    tmima_en = models.CharField(max_length=5)
    homepage = models.TextField()
    homepage_en = models.TextField()
    lastupdate = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'department'

class Instructors(models.Model):
    instr_id = models.IntegerField(primary_key=True)
    cv = models.TextField(blank=True)
    cv_en = models.TextField(blank=True)
    research = models.TextField(blank=True)
    research_en = models.TextField(blank=True)
    subject = models.CharField(max_length=255, blank=True)
    subject_en = models.CharField(max_length=255, blank=True)
    lastupdate = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'instructors'

class Katefth(models.Model):
    kat_id = models.IntegerField(primary_key=True)
    perigrafi_kat = models.CharField(max_length=100)
    perigrafi_kat_en = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'katefth'

class KatefthKykloi(models.Model):
    kat_id = models.IntegerField()
    kyklos_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'katefth_kykloi'

class Kykloi(models.Model):
    kyklos_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    name_en = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    notes_en = models.TextField(blank=True)
    dept_id = models.IntegerField(blank=True, null=True)
    examina = models.IntegerField()
    indexing = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'kykloi'

class KykloiExamina(models.Model):
    id = models.IntegerField(primary_key=True)
    examina = models.TextField()
    notes = models.CharField(max_length=255, blank=True)
    notes_en = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'kykloi_examina'

class ModuleKykloi(models.Model):
    module_id = models.IntegerField()
    kyklos_id = models.IntegerField()
    semester = models.IntegerField()
    indexing = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'module_kykloi'

class Modules(models.Model):
    id = models.IntegerField(primary_key=True)
    module = models.CharField(max_length=255)
    description = models.TextField()
    choice = models.IntegerField()
    module_en = models.CharField(max_length=255)
    description_en = models.TextField()
    notes = models.CharField(max_length=255)
    notes_en = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'modules'

class ModulesTutors(models.Model):
    module_id = models.IntegerField()
    tutor_id = models.IntegerField()
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'modules_tutors'

class PubInstr(models.Model):
    pubid = models.IntegerField()
    instrid = models.IntegerField()
    cduom = models.IntegerField()
    lastupdate = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'pub_instr'

class PubTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    type_description = models.CharField(max_length=255)
    lastupdate = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'pub_types'

class Publications(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.TextField()
    year = models.CharField(max_length=4)
    typeid = models.IntegerField()
    filelink = models.CharField(max_length=255, blank=True)
    pubdate = models.DateField(blank=True, null=True)
    lastupdate = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'publications'

class Ranks(models.Model):
    rank_id = models.IntegerField(primary_key=True)
    idiotita_per = models.CharField(max_length=150)
    idiotita_per_en = models.CharField(max_length=150)
    notes = models.CharField(max_length=250, blank=True)
    class Meta:
        managed = False
        db_table = 'ranks'

class Service(models.Model):
    service_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    name_en = models.CharField(max_length=150, blank=True)
    notes = models.TextField(blank=True)
    notes_en = models.TextField(blank=True)
    is_academic = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'service'

class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=4)
    status = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'users'

class Works(models.Model):
    emp_id = models.IntegerField()
    service_id = models.IntegerField()
    attribute_id = models.IntegerField()
    phone = models.CharField(max_length=36, blank=True)
    primary_academic = models.IntegerField()
    lastupdate = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'works'

