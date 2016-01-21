from google.appengine.ext import ndb

class Post(ndb.Model):
	blood_sugar = ndb.StringProperty(required=True)
	insulin = ndb.StringProperty(required=True)
	food = ndb.StringProperty(required=True)
	page_date = ndb.StringProperty(required=True)
	adddate = ndb.DateTimeProperty(auto_now_add=True)