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

attr_data = []

class Attributes(models.Model):
    attr_id = models.AutoField(max_length=11, primary_key=True, verbose_name="Id")
    descr = models.CharField(max_length=140, verbose_name="Description")
    descr_en = models.CharField(max_length=140, verbose_name="English Description")
    notes = models.CharField(max_length=250, blank=True, verbose_name="Notes")
    class Meta:
        db_table = 'attributes'
        verbose_name= 'Attributes'
    def __unicode__(self):
          return unicode(self.attr_id)
<<<<<<< HEAD
=======
    def get_field(self,field):
		if field == self.attr_id:
			return self.attr_id
		elif field == self.descr:
			return self.descr
		elif field == self.descr_en:
			return self.descr_en
		else:
			return self.notes
>>>>>>> afa76c68ac52b11cb70ac2e2a930c939c00d4e7f

class Employees(models.Model):
    emp_id = models.AutoField(primary_key=True, verbose_name="Id")
    lastname = models.CharField(max_length=110, verbose_name="Last name")
    lastname_en = models.CharField(max_length=110, blank=True, verbose_name="Last name english") 
    firstname = models.CharField(max_length=50, verbose_name="First name")
    firstname_en = models.CharField(max_length=50, blank=True, verbose_name="First name english")
    phone_home = models.CharField(max_length=12, blank=True, verbose_name="Home phone") 
    phone_home_view = models.IntegerField(max_length=1, default='0', verbose_name="Home phone view") 
    phone_mobile = models.CharField(max_length=12, blank=True, verbose_name="Mobile phone")
    phone_mobile_view = models.IntegerField(max_length=1, default='0', verbose_name="Mobile phone view") 
    email = models.CharField(max_length=50, blank=True, verbose_name="Email") 
    fax = models.CharField(max_length=12, blank=True, verbose_name="FAX") 
    url = models.CharField(max_length=70, blank=True, verbose_name="URL") 
    photo_path = models.CharField(max_length=70, blank=True, verbose_name="Photo path") 
    office = models.CharField(max_length=70, blank=True, verbose_name="Office") 
    building = models.CharField(max_length=70, blank=True, verbose_name="Building")
    office_en = models.CharField(max_length=70, blank=True, verbose_name="Office english") 
    building_en = models.CharField(max_length=70, blank=True, verbose_name="Building english")
    address_home = models.CharField(max_length=150, blank=True, verbose_name="Home address")
    zip_home = models.CharField(max_length=10, blank=True, verbose_name="Home zip code")
    city = models.CharField(max_length=110, blank=True, verbose_name="City") 
    address_view = models.IntegerField(max_length=1, default='0', verbose_name="Address view")
    rank_id = models.IntegerField(max_length=11, default='1', verbose_name="Rank id")
    notes = models.CharField(max_length=255, blank=True, verbose_name="Notes") 
    public_view = models.IntegerField(max_length=1, default='1', verbose_name="Public view") 
    middlename = models.CharField(max_length=3, blank=True, verbose_name="Middle name") 
    middlename_en = models.CharField(max_length=3, blank=True, verbose_name="Middle name english") 
    last_update = models.DateTimeField(verbose_name="last update")
#default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
    class Meta:
        db_table = 'employees'
        verbose_name= 'Employees'
    def __unicode__(self):
        return u'%s !!!! %s' % (self.firstname, self.lastname)

class Department(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    tmima_per = models.TextField(verbose_name="tmima peri")
    proedros = models.IntegerField(default='0', verbose_name="proedros")
    pr_spoudwn = models.TextField(verbose_name="Programma spoudwn")
    pr_spoudwn_en = models.TextField(verbose_name="Program spoudwn english")
    tmima_per_en = models.TextField(verbose_name="tmima period english")
    tmima_en = models.CharField(max_length=5, verbose_name="tmima english")
    homepage = models.TextField(verbose_name="Homepage")
    homepage_en = models.TextField(verbose_name="Homepage english")
    lastupdate = models.DateTimeField(verbose_name="last update")
    class Meta:
        db_table = 'department'
        verbose_name= 'Department'
    def __unicode__(self):
        return u'%s !!!! %s !!!! %s !!!! %s !!!!!' % (self.tmima_en, self.lastupdate, self.proedros, self.pr_spoudwn)

class Instructors(models.Model):
    instr_id = models.AutoField(primary_key=True, default='0', verbose_name="Id")
    cv = models.TextField(blank=True, verbose_name="curiculum vitae")
    cv_en = models.TextField(blank=True, verbose_name="curiculum vitae en")
    research = models.TextField(blank=True, verbose_name="research")
    research_en = models.TextField(blank=True, verbose_name="Research english")
    subject = models.CharField(max_length=255, blank=True, verbose_name="subject")
    subject_en = models.CharField(max_length=255, blank=True, verbose_name="English subject")
    activities = models.TextField(blank=True, verbose_name="activities") 
    activities_en = models.TextField(blank=True, verbose_name="activities english")
    lastupdate = models.DateTimeField(verbose_name="last update")
    class Meta:
        db_table = 'instructors'
        verbose_name= 'Instructors'
    def __unicode__(self):
        return u'%s' % self.subject
######
def __init__(self, *args, **kwargs):
    super(CircuitForm, self).__init__(*args, **kwargs)
    for f_name in self.fields:
        self.fields[f_name].required = False
#######
class Katefth(models.Model):
    kat_id = models.AutoField(primary_key=True, verbose_name="Id")
    perigrafi_kat = models.CharField(max_length=100, verbose_name="perigrafi katefthnsh")
    perigrafi_kat_en = models.CharField(max_length=100, verbose_name="perigrafi katefthnsh english")
    class Meta:
        db_table = 'katefth'
        verbose_name= 'Katefthnsh'
    def __unicode__(self):
        return self.perigrafi_kat

class KatefthKykloi(models.Model):
    kat_id = models.IntegerField(primary_key=True, verbose_name="Id katefthnsh")
    kyklos_id = models.IntegerField(verbose_name="kykloi id")
    class Meta:
        db_table = 'katefthKykloi'
        unique_together = ("kat_id", "kyklos_id")
        verbose_name= 'Katefthnsh kykloi'
    def __unicode__(self):
        return self.kat_id
	unique_together = ("kat_id", "kyklos_id")
	verbose_name= 'Katefthnsh kykloi'

class Kykloi(models.Model):
    kyklos_id = models.AutoField(primary_key=True, verbose_name="Id")
    name = models.CharField(max_length=255, blank=True, verbose_name="name")
    name_en = models.CharField(max_length=255, blank=True, verbose_name="name english")
    notes = models.TextField(blank=True, verbose_name="Notes")
    notes_en = models.TextField(blank=True, verbose_name="Notes english")
    dept_id = models.IntegerField(blank=True, null=True, verbose_name="department id")
    examina = models.IntegerField(verbose_name="examina")
    indexing = models.IntegerField(default='0000', verbose_name="indexing")
    class Meta:
        db_table = 'kykloi'
        verbose_name= 'Kykloi'
    def __unicode__(self):
        return self.name

class KykloiExamina(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    examina = models.TextField(verbose_name="examina")
    notes = models.CharField(max_length=255, blank=True, verbose_name="notes")
    notes_en = models.CharField(max_length=255, blank=True, verbose_name="notes_en")
    comments = models.TextField(blank=True, verbose_name="comments")
    class Meta:
        db_table = 'kykloiExamina'
        verbose_name= 'Kykloi examina'
    def __unicode__(self):
        return self.notes
	verbose_name= 'Kykloi examina'

class ModuleKykloi(models.Model):
    module_id = models.IntegerField(primary_key=True, default='0', verbose_name="module_id")
    kyklos_id = models.IntegerField(default='0', verbose_name="kyklos_id")
    semester = models.IntegerField(default='0', verbose_name="semester")
    indexing = models.IntegerField(default='99', verbose_name="indexing")
    class Meta:
        db_table = 'moduleKykloi'
        unique_together = (("module_id", "kyklos_id", "semester"),)
        verbose_name= 'Modules Kyklwn'
    def __unicode__(self):
        return self.semester
	unique_together = (("module_id", "kyklos_id", "semester"),)
	verbose_name= 'Modules Kyklwn'

class Modules(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    module = models.CharField(max_length=255, default='', verbose_name="module")
    description = models.TextField(verbose_name="description")
    choice = models.IntegerField(default='0', verbose_name="choice")
    module_en = models.CharField(max_length=255, default='', verbose_name="module_en")
    description_en = models.TextField(verbose_name="description_en")
    notes = models.CharField(max_length=255, default='', verbose_name="notes")
    notes_en = models.CharField(max_length=255, verbose_name="notes_en")
    class Meta:
        db_table = 'modules'
        verbose_name= 'Modules'
    def __unicode__(self):
        return self.description

class ModulesTutors(models.Model):
    module_id = models.IntegerField(primary_key=True, default='0', verbose_name="module_id")
    tutor_id = models.IntegerField(default='0', verbose_name="tutor_id")
    last_update = models.DateTimeField(verbose_name="last_update")
    class Meta:
        db_table = 'modulesTutors'
        unique_together = (("module_id", "tutor_id"),)
        verbose_name= 'Modules tutors'
    def __unicode__(self):
        return self.last_update
	unique_together = (("module_id", "tutor_id"),)
	verbose_name= 'Modules tutors'

class PubInstr(models.Model):
    pubid = models.IntegerField(primary_key=True, default='0', verbose_name="pubid")
    instrid = models.IntegerField(default='0', verbose_name="instrid")
    cduom = models.IntegerField(default='1', verbose_name="cduom")
    lastupdate = models.DateTimeField(verbose_name="lastupdate")
    class Meta:
        db_table = 'pubInstr'
        unique_together = (("pubid", "instrid"),)
        verbose_name= 'Publication instr'
    def __unicode__(self):
        return self.lastupdate
	unique_together = (("pubid", "instrid"),)
	verbose_name= 'Publication instr'

class PubTypes(models.Model):
    id = models.AutoField(primary_key=True, default='0', verbose_name="id")
    type_description = models.CharField(max_length=255, verbose_name=" type_description")
    lastupdate = models.DateTimeField(verbose_name="lastupdate")
    class Meta:
        db_table = 'pubTypes'
        verbose_name= 'Publication types'
    def __unicode__(self):
        return self.lastupdate
	verbose_name= 'Publication types'

class Publications(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    description = models.TextField(verbose_name="description")
    year = models.CharField(max_length=4, default='', verbose_name="year")
    typeid = models.IntegerField(default='0', verbose_name="typeid")
    filelink = models.CharField(max_length=255, blank=True, verbose_name="filelink")
    pubdate = models.DateField(blank=True, null=True, verbose_name="pubdate")
    lastupdate = models.DateTimeField(verbose_name="lastupdate")
    class Meta:
        db_table = 'publications'
        verbose_name= 'Publications'
    def __unicode__(self):
        return self.year

class Ranks(models.Model):
    rank_id = models.AutoField(primary_key=True, verbose_name="rank_id")
    idiotita_per = models.CharField(max_length=150, default='', verbose_name="idiotita_per")
    idiotita_per_en = models.CharField(max_length=150, default='', verbose_name="idiotita_per_en")
    notes = models.CharField(max_length=250, blank=True, verbose_name="notes")
    class Meta:
        db_table = 'ranks'
        verbose_name= 'Ranks'
    def __unicode__(self):
        return self.idiotita_per

class Service(models.Model):
    service_id = models.AutoField(primary_key=True, verbose_name="service_id")
    name = models.CharField(max_length=150, blank=True, verbose_name="name")
    name_en = models.CharField(max_length=150, blank=True, verbose_name="name_en")
    notes = models.TextField(blank=True, verbose_name="notes")
    notes_en = models.TextField(blank=True, verbose_name="notes_en")
    is_academic = models.IntegerField(default='0', verbose_name="is_academic")
    class Meta:
        db_table = 'service'
        verbose_name= 'Service'
    def __unicode__(self):
        return self.name

class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=20, default='', verbose_name="username")
    password = models.CharField(max_length=4, default='ldap', verbose_name="password")
    status = models.IntegerField(default='1', verbose_name="status")
    class Meta:
        db_table = 'users'
        verbose_name= 'Users'
    def __unicode__(self):
        return self.username

class Works(models.Model):
    emp_id = models.IntegerField(primary_key=True, verbose_name="emp_id")
    service_id = models.IntegerField(verbose_name="service_id")
    attribute_id = models.IntegerField(default='44', verbose_name="attribute_id")
    phone = models.CharField(max_length=36, blank=True, verbose_name="phone")
    primary_academic = models.IntegerField(verbose_name="primary_academic")
    lastupdate = models.DateTimeField(verbose_name="lastupdate")
    class Meta:
        db_table = 'works'
        unique_together = (("emp_id", "service_id", "attribute_id"),)
        verbose_name= 'Works'
    def __unicode__(self):
        return self.phone

