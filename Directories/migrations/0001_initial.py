# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attributes'
        db.create_table(u'attributes', (
            ('attr_id', self.gf('django.db.models.fields.AutoField')(max_length=11, primary_key=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('descr_en', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal(u'Directories', ['Attributes'])

        # Adding model 'Employees'
        db.create_table(u'employees', (
            ('emp_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=110)),
            ('lastname_en', self.gf('django.db.models.fields.CharField')(max_length=110, blank=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('firstname_en', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('phone_home', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('phone_home_view', self.gf('django.db.models.fields.IntegerField')(default=u'0', max_length=1)),
            ('phone_mobile', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('phone_mobile_view', self.gf('django.db.models.fields.IntegerField')(default=u'0', max_length=1)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('photo_path', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('office', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('office_en', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('building_en', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('address_home', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('zip_home', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=110, blank=True)),
            ('address_view', self.gf('django.db.models.fields.IntegerField')(default=u'0', max_length=1)),
            ('rank_id', self.gf('django.db.models.fields.IntegerField')(default=u'1', max_length=11)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('public_view', self.gf('django.db.models.fields.IntegerField')(default=u'1', max_length=1)),
            ('middlename', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('middlename_en', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Directories', ['Employees'])

        # Adding model 'Department'
        db.create_table(u'department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tmima_per', self.gf('django.db.models.fields.TextField')()),
            ('proedros', self.gf('django.db.models.fields.IntegerField')(default=u'0')),
            ('pr_spoudwn', self.gf('django.db.models.fields.TextField')()),
            ('pr_spoudwn_en', self.gf('django.db.models.fields.TextField')()),
            ('tmima_per_en', self.gf('django.db.models.fields.TextField')()),
            ('tmima_en', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('homepage', self.gf('django.db.models.fields.TextField')()),
            ('homepage_en', self.gf('django.db.models.fields.TextField')()),
            ('lastupdate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Directories', ['Department'])

        # Adding model 'Instructors'
        db.create_table(u'instructors', (
            ('instr_id', self.gf('django.db.models.fields.AutoField')(default=u'0', primary_key=True)),
            ('cv', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cv_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('research', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('research_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('subject_en', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('activities', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('activities_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lastupdate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Directories', ['Instructors'])

        # Adding model 'Katefth'
        db.create_table(u'katefth', (
            ('kat_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('perigrafi_kat', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('perigrafi_kat_en', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'Directories', ['Katefth'])

        # Adding model 'KatefthKykloi'
        db.create_table(u'katefth_kykloi', (
            ('kat_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('kyklos_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'Directories', ['KatefthKykloi'])

        # Adding unique constraint on 'KatefthKykloi', fields ['kat_id', 'kyklos_id']
        db.create_unique(u'katefth_kykloi', ['kat_id', 'kyklos_id'])

        # Adding model 'Kykloi'
        db.create_table(u'kykloi', (
            ('kyklos_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('notes_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('dept_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('examina', self.gf('django.db.models.fields.IntegerField')()),
            ('indexing', self.gf('django.db.models.fields.IntegerField')(default=u'0000')),
        ))
        db.send_create_signal(u'Directories', ['Kykloi'])

        # Adding model 'KykloiExamina'
        db.create_table(u'kykloiExamina', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('examina', self.gf('django.db.models.fields.TextField')()),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('notes_en', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'Directories', ['KykloiExamina'])

        # Adding model 'ModuleKykloi'
        db.create_table(u'moduleKykloi', (
            ('module_id', self.gf('django.db.models.fields.IntegerField')(default=u'0', primary_key=True)),
            ('kyklos_id', self.gf('django.db.models.fields.IntegerField')(default=u'0')),
            ('semester', self.gf('django.db.models.fields.IntegerField')(default=u'0')),
            ('indexing', self.gf('django.db.models.fields.IntegerField')(default=u'99')),
        ))
        db.send_create_signal(u'Directories', ['ModuleKykloi'])

        # Adding unique constraint on 'ModuleKykloi', fields ['module_id', 'kyklos_id', 'semester']
        db.create_unique(u'moduleKykloi', ['module_id', 'kyklos_id', 'semester'])

        # Adding model 'Modules'
        db.create_table(u'modules', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('module', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('choice', self.gf('django.db.models.fields.IntegerField')(default=u'0')),
            ('module_en', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255)),
            ('description_en', self.gf('django.db.models.fields.TextField')()),
            ('notes', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255)),
            ('notes_en', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'Directories', ['Modules'])

        # Adding model 'ModulesTutors'
        db.create_table(u'modulesTutors', (
            ('module_id', self.gf('django.db.models.fields.IntegerField')(default=u'0', primary_key=True)),
            ('tutor_id', self.gf('django.db.models.fields.IntegerField')(default=u'0')),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Directories', ['ModulesTutors'])

        # Adding unique constraint on 'ModulesTutors', fields ['module_id', 'tutor_id']
        db.create_unique(u'modulesTutors', ['module_id', 'tutor_id'])

        # Adding model 'PubInstr'
        db.create_table(u'pubInstr', (
            ('pubid', self.gf('django.db.models.fields.IntegerField')(default=u'0', primary_key=True)),
            ('instrid', self.gf('django.db.models.fields.IntegerField')(default=u'0')),
            ('cduom', self.gf('django.db.models.fields.IntegerField')(default=u'1')),
            ('lastupdate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Directories', ['PubInstr'])

        # Adding unique constraint on 'PubInstr', fields ['pubid', 'instrid']
        db.create_unique(u'pubInstr', ['pubid', 'instrid'])

        # Adding model 'PubTypes'
        db.create_table(u'pubTypes', (
            ('id', self.gf('django.db.models.fields.AutoField')(default=u'0', primary_key=True)),
            ('type_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Directories', ['PubTypes'])

        # Adding model 'Publications'
        db.create_table(u'publications', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('year', self.gf('django.db.models.fields.CharField')(default=u'', max_length=4)),
            ('typeid', self.gf('django.db.models.fields.IntegerField')(default=u'0')),
            ('filelink', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('pubdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('lastupdate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Directories', ['Publications'])

        # Adding model 'Ranks'
        db.create_table(u'ranks', (
            ('rank_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idiotita_per', self.gf('django.db.models.fields.CharField')(default=u'', max_length=150)),
            ('idiotita_per_en', self.gf('django.db.models.fields.CharField')(default=u'', max_length=150)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal(u'Directories', ['Ranks'])

        # Adding model 'Service'
        db.create_table(u'service', (
            ('service_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('notes_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_academic', self.gf('django.db.models.fields.IntegerField')(default=u'0')),
        ))
        db.send_create_signal(u'Directories', ['Service'])

        # Adding model 'Users'
        db.create_table(u'users', (
            ('username', self.gf('django.db.models.fields.CharField')(default=u'', max_length=20, primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(default=u'ldap', max_length=4)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=u'1')),
        ))
        db.send_create_signal(u'Directories', ['Users'])

        # Adding model 'Works'
        db.create_table(u'works', (
            ('emp_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('service_id', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute_id', self.gf('django.db.models.fields.IntegerField')(default=u'44')),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('primary_academic', self.gf('django.db.models.fields.IntegerField')()),
            ('lastupdate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Directories', ['Works'])

        # Adding unique constraint on 'Works', fields ['emp_id', 'service_id', 'attribute_id']
        db.create_unique(u'works', ['emp_id', 'service_id', 'attribute_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Works', fields ['emp_id', 'service_id', 'attribute_id']
        db.delete_unique(u'works', ['emp_id', 'service_id', 'attribute_id'])

        # Removing unique constraint on 'PubInstr', fields ['pubid', 'instrid']
        db.delete_unique(u'pubInstr', ['pubid', 'instrid'])

        # Removing unique constraint on 'ModulesTutors', fields ['module_id', 'tutor_id']
        db.delete_unique(u'modulesTutors', ['module_id', 'tutor_id'])

        # Removing unique constraint on 'ModuleKykloi', fields ['module_id', 'kyklos_id', 'semester']
        db.delete_unique(u'moduleKykloi', ['module_id', 'kyklos_id', 'semester'])

        # Removing unique constraint on 'KatefthKykloi', fields ['kat_id', 'kyklos_id']
        db.delete_unique(u'katefth_kykloi', ['kat_id', 'kyklos_id'])

        # Deleting model 'Attributes'
        db.delete_table(u'attributes')

        # Deleting model 'Employees'
        db.delete_table(u'employees')

        # Deleting model 'Department'
        db.delete_table(u'department')

        # Deleting model 'Instructors'
        db.delete_table(u'instructors')

        # Deleting model 'Katefth'
        db.delete_table(u'katefth')

        # Deleting model 'KatefthKykloi'
        db.delete_table(u'katefth_kykloi')

        # Deleting model 'Kykloi'
        db.delete_table(u'kykloi')

        # Deleting model 'KykloiExamina'
        db.delete_table(u'kykloiExamina')

        # Deleting model 'ModuleKykloi'
        db.delete_table(u'moduleKykloi')

        # Deleting model 'Modules'
        db.delete_table(u'modules')

        # Deleting model 'ModulesTutors'
        db.delete_table(u'modulesTutors')

        # Deleting model 'PubInstr'
        db.delete_table(u'pubInstr')

        # Deleting model 'PubTypes'
        db.delete_table(u'pubTypes')

        # Deleting model 'Publications'
        db.delete_table(u'publications')

        # Deleting model 'Ranks'
        db.delete_table(u'ranks')

        # Deleting model 'Service'
        db.delete_table(u'service')

        # Deleting model 'Users'
        db.delete_table(u'users')

        # Deleting model 'Works'
        db.delete_table(u'works')


    models = {
        u'Directories.attributes': {
            'Meta': {'object_name': 'Attributes', 'db_table': "u'attributes'"},
            'attr_id': ('django.db.models.fields.AutoField', [], {'max_length': '11', 'primary_key': 'True'}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'descr_en': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        u'Directories.department': {
            'Meta': {'object_name': 'Department', 'db_table': "u'department'"},
            'homepage': ('django.db.models.fields.TextField', [], {}),
            'homepage_en': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastupdate': ('django.db.models.fields.DateTimeField', [], {}),
            'pr_spoudwn': ('django.db.models.fields.TextField', [], {}),
            'pr_spoudwn_en': ('django.db.models.fields.TextField', [], {}),
            'proedros': ('django.db.models.fields.IntegerField', [], {'default': "u'0'"}),
            'tmima_en': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'tmima_per': ('django.db.models.fields.TextField', [], {}),
            'tmima_per_en': ('django.db.models.fields.TextField', [], {})
        },
        u'Directories.employees': {
            'Meta': {'object_name': 'Employees', 'db_table': "u'employees'"},
            'address_home': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'address_view': ('django.db.models.fields.IntegerField', [], {'default': "u'0'", 'max_length': '1'}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'building_en': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '110', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'emp_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'firstname_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '110'}),
            'lastname_en': ('django.db.models.fields.CharField', [], {'max_length': '110', 'blank': 'True'}),
            'middlename': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'middlename_en': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'office': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'office_en': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'phone_home': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'phone_home_view': ('django.db.models.fields.IntegerField', [], {'default': "u'0'", 'max_length': '1'}),
            'phone_mobile': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'phone_mobile_view': ('django.db.models.fields.IntegerField', [], {'default': "u'0'", 'max_length': '1'}),
            'photo_path': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'public_view': ('django.db.models.fields.IntegerField', [], {'default': "u'1'", 'max_length': '1'}),
            'rank_id': ('django.db.models.fields.IntegerField', [], {'default': "u'1'", 'max_length': '11'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'zip_home': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'Directories.instructors': {
            'Meta': {'object_name': 'Instructors', 'db_table': "u'instructors'"},
            'activities': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'activities_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cv': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cv_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'instr_id': ('django.db.models.fields.AutoField', [], {'default': "u'0'", 'primary_key': 'True'}),
            'lastupdate': ('django.db.models.fields.DateTimeField', [], {}),
            'research': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'research_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'subject_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'Directories.katefth': {
            'Meta': {'object_name': 'Katefth', 'db_table': "u'katefth'"},
            'kat_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perigrafi_kat': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'perigrafi_kat_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'Directories.katefthkykloi': {
            'Meta': {'unique_together': "((u'kat_id', u'kyklos_id'),)", 'object_name': 'KatefthKykloi', 'db_table': "u'katefth_kykloi'"},
            'kat_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'kyklos_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Directories.kykloi': {
            'Meta': {'object_name': 'Kykloi', 'db_table': "u'kykloi'"},
            'dept_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'examina': ('django.db.models.fields.IntegerField', [], {}),
            'indexing': ('django.db.models.fields.IntegerField', [], {'default': "u'0000'"}),
            'kyklos_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'notes_en': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'Directories.kykloiexamina': {
            'Meta': {'object_name': 'KykloiExamina', 'db_table': "u'kykloiExamina'"},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examina': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'Directories.modulekykloi': {
            'Meta': {'unique_together': "((u'module_id', u'kyklos_id', u'semester'),)", 'object_name': 'ModuleKykloi', 'db_table': "u'moduleKykloi'"},
            'indexing': ('django.db.models.fields.IntegerField', [], {'default': "u'99'"}),
            'kyklos_id': ('django.db.models.fields.IntegerField', [], {'default': "u'0'"}),
            'module_id': ('django.db.models.fields.IntegerField', [], {'default': "u'0'", 'primary_key': 'True'}),
            'semester': ('django.db.models.fields.IntegerField', [], {'default': "u'0'"})
        },
        u'Directories.modules': {
            'Meta': {'object_name': 'Modules', 'db_table': "u'modules'"},
            'choice': ('django.db.models.fields.IntegerField', [], {'default': "u'0'"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255'}),
            'module_en': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255'}),
            'notes': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255'}),
            'notes_en': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'Directories.modulestutors': {
            'Meta': {'unique_together': "((u'module_id', u'tutor_id'),)", 'object_name': 'ModulesTutors', 'db_table': "u'modulesTutors'"},
            'last_update': ('django.db.models.fields.DateTimeField', [], {}),
            'module_id': ('django.db.models.fields.IntegerField', [], {'default': "u'0'", 'primary_key': 'True'}),
            'tutor_id': ('django.db.models.fields.IntegerField', [], {'default': "u'0'"})
        },
        u'Directories.pubinstr': {
            'Meta': {'unique_together': "((u'pubid', u'instrid'),)", 'object_name': 'PubInstr', 'db_table': "u'pubInstr'"},
            'cduom': ('django.db.models.fields.IntegerField', [], {'default': "u'1'"}),
            'instrid': ('django.db.models.fields.IntegerField', [], {'default': "u'0'"}),
            'lastupdate': ('django.db.models.fields.DateTimeField', [], {}),
            'pubid': ('django.db.models.fields.IntegerField', [], {'default': "u'0'", 'primary_key': 'True'})
        },
        u'Directories.publications': {
            'Meta': {'object_name': 'Publications', 'db_table': "u'publications'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'filelink': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastupdate': ('django.db.models.fields.DateTimeField', [], {}),
            'pubdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'typeid': ('django.db.models.fields.IntegerField', [], {'default': "u'0'"}),
            'year': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '4'})
        },
        u'Directories.pubtypes': {
            'Meta': {'object_name': 'PubTypes', 'db_table': "u'pubTypes'"},
            'id': ('django.db.models.fields.AutoField', [], {'default': "u'0'", 'primary_key': 'True'}),
            'lastupdate': ('django.db.models.fields.DateTimeField', [], {}),
            'type_description': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'Directories.ranks': {
            'Meta': {'object_name': 'Ranks', 'db_table': "u'ranks'"},
            'idiotita_per': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '150'}),
            'idiotita_per_en': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '150'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'rank_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Directories.service': {
            'Meta': {'object_name': 'Service', 'db_table': "u'service'"},
            'is_academic': ('django.db.models.fields.IntegerField', [], {'default': "u'0'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'notes_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'service_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Directories.users': {
            'Meta': {'object_name': 'Users', 'db_table': "u'users'"},
            'password': ('django.db.models.fields.CharField', [], {'default': "u'ldap'", 'max_length': '4'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': "u'1'"}),
            'username': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '20', 'primary_key': 'True'})
        },
        u'Directories.works': {
            'Meta': {'unique_together': "((u'emp_id', u'service_id', u'attribute_id'),)", 'object_name': 'Works', 'db_table': "u'works'"},
            'attribute_id': ('django.db.models.fields.IntegerField', [], {'default': "u'44'"}),
            'emp_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'lastupdate': ('django.db.models.fields.DateTimeField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'primary_academic': ('django.db.models.fields.IntegerField', [], {}),
            'service_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['Directories']