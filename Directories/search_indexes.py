# if new model indexes are inserted run: "sudo python manage.py rebuild_index"
import datetime
import haystack
from haystack import indexes
from Directories.models import Attributes, Employees, Department, Instructors, Katefth, KatefthKykloi, Kykloi, KykloiExamina, ModuleKykloi, Modules, ModulesTutors, PubInstr, PubTypes, Publications, Ranks, Service, Users, Works

class AttributesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    descr = indexes.CharField(model_attr='descr') 
    descr_en = indexes.CharField(model_attr='descr_en')
    #notes = indexes.CharField(model_attr='notes') --> notes has only null values, no point indexing
    def get_model(self):
        return Attributes
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all() #filter(descr_en='Dean')

class EmployeesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    lastname = indexes.CharField(model_attr='lastname')
    #lastname_en = indexes.CharField(model_attr='lastname_en') 
    firstname = indexes.CharField(model_attr='firstname')
    #firstname_en = indexes.CharField(model_attr='firstname_en')
    #phone_home = indexes.CharField(model_attr='phone_home') 
    phone_home_view = indexes.IntegerField(model_attr='phone_home_view') 
    #phone_mobile = indexes.CharField(model_attr='phone_mobile')
    phone_mobile_view = indexes.IntegerField(model_attr='phone_mobile_view') 
    #email = indexes.CharField(model_attr='email') 
    #fax = indexes.CharField(model_attr='fax') 
    #url = indexes.CharField(model_attr='url') 
    #photo_path = indexes.CharField(model_attr='photo_path') 
    #office = indexes.CharField(model_attr='office') 
    #building = indexes.CharField(model_attr='building')
    #office_en = indexes.CharField(model_attr='office_en') 
    #building_en = indexes.CharField(model_attr='building_en') 
    #address_home = indexes.CharField(model_attr='address_home') 
    #zip_home = indexes.CharField(model_attr='zip_home') 
    #city = indexes.CharField(model_attr='city') 
    address_view = indexes.IntegerField(model_attr='address_view') 
    rank_id = indexes.IntegerField(model_attr='rank_id') 
    #notes = indexes.CharField(model_attr='notes') 
    public_view = indexes.IntegerField(model_attr='public_view') 
    #middlename = indexes.CharField(model_attr='middlename') 
    #middlename_en = indexes.CharField(model_attr='middlename_en')  
    last_update = indexes.DateTimeField(model_attr='last_update') 
    def get_model(self):
        return Employees
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all() #filter(descr_en='Dean')
'''
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

class Katefth(models.Model):
    kat_id = models.AutoField(primary_key=True, verbose_name="Id")
    perigrafi_kat = models.CharField(blank=True, max_length=100, verbose_name="perigrafi katefthnsh")
    perigrafi_kat_en = models.CharField(blank=True, max_length=100, verbose_name="perigrafi katefthnsh english")
    class Meta:
        db_table = 'katefth'
        verbose_name= 'Katefth' 
             
class KatefthKykloi(models.Model):
    kat_id = models.IntegerField(primary_key=True, verbose_name="Id katefthnsh")
    kyklos_id = models.IntegerField(verbose_name="kykloi id")
    class Meta:
        db_table = 'katefth_kykloi'
        unique_together = ("kat_id", "kyklos_id")
        verbose_name= 'KatefthKykloi'

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
        db_table = 'kykloi_examina'
        verbose_name= 'kykloi_examina'

class ModuleKykloi(models.Model):
    module_id = models.IntegerField(primary_key=True, default='0', verbose_name="module_id")
    kyklos_id = models.IntegerField(default='0', verbose_name="kyklos_id")
    semester = models.IntegerField(default='0', verbose_name="semester")
    indexing = models.IntegerField(default='99', verbose_name="indexing")
    class Meta:
        db_table = 'module_kykloi'
        unique_together = (("module_id", "kyklos_id", "semester"),)
        verbose_name= 'ModuleKykloi'
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
        db_table = 'modules_tutors'
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

class PubTypes(models.Model):
    id = models.AutoField(primary_key=True, default='0', verbose_name="id")
    type_description = models.CharField(max_length=255, verbose_name=" type_description")
    lastupdate = models.DateTimeField(verbose_name="lastupdate")
    class Meta:
        db_table = 'pubTypes'
        verbose_name= 'Publication Types'
    def __unicode__(self):
        return self.lastupdate

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


'''

'''example TweetSite

class tweetModel(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=30)
	body = models.TextField(max_length=140)
	timestamp = models.DateTimeField()
		
class TweetIndex(RealTimeSearchIndex):
	text = CharField(document=True)
	body = CharField(model_attr='body')
	author = CharField(model_attr='author')
	title = CharField(model_attr='title')
	def prepare(self, obj):
		self.prepared_data = super(TweetIndex, self).prepare(obj)
		self.prepared_data['text'] = obj.body, obj.title, obj.author
		return self.prepared_data
site.register(tweetModel, TweetIndex)


'''
