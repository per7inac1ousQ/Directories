# if new model indexes are inserted run: "sudo python manage.py rebuild_index"
import datetime
from haystack import indexes
from Directories.models import Attributes

class AttributesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True) #use_template=True???
    descr = indexes.CharField(model_attr='descr') 
    descr_en = indexes.CharField(model_attr='descr_en')
    #notes = indexes.CharField(model_attr='notes') --> notes has only null values, no point indexing
    def get_model(self):
        return Attributes
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()#filter(attr_id__lte=99)
  
  
    
''' text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    
    attr_id = indexes.AutoField()
    descr = indexes.CharField(document=True,  use_template=True) 
    descr_en = indexes.CharField(model_attr='descr_en')
    notes = indexes.CharField(model_attr='notes')
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
