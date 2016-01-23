from google.appengine.api import users
import webapp2
import jinja2
import os
from google.appengine.ext import db
from google.appengine.ext import ndb
import datetime
from datetime import datetime, timedelta
import time
import json
import models

# This will set the variable with the template path.
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

def render_str(template, **params):
	t = jinja_env.get_template(template)
	return t.render(params)

class BaseHandler(webapp2.RequestHandler):
	def render(self, template, **kw):
		self.response.out.write(render_str(template, **kw))

	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

class MyHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))

        self.response.out.write('<html><body>%s</body></html>' % greeting)

class Home(BaseHandler):
	def get(self):
		if self.request.get('fmt'):
			page_date_result = self.request.get('fmt')
			qry = models.Post.query(models.Post.page_date == page_date_result)
			print 'triggered'
			json_append = []
			for items in qry:
			  item_dict = items.to_dict()
			  date_format = item_dict.get('adddate')
			  if date_format:
			    item_dict['adddate'] = str(date_format)
			
			  json_append.append(item_dict)
			print 'pooper'
			print json_append
			self.response.out.headers['Content-Type'] = 'text/json'
			self.response.out.write(json.dumps(json_append))
			return

		self.render('index.html')

	def post(self):
		blood_sugar = self.request.get('blood_sugar')
		insulin = self.request.get('insulin')
		food = self.request.get('food')
		page_date = self.request.get('date_entry')

		new_post = models.Post(blood_sugar=blood_sugar, insulin=insulin, food=food, page_date=page_date)
		new_post.put()
		self.redirect('/')

class About(BaseHandler):
	def get(self):
		self.render('about.html')

	def tester(self, stuff):
		qry = models.Post.query(models.Post.page_date == stuff)
		json_append = []
		for items in stuff:
		  item_dict = items.to_dict()
		  date_format = item_dict.get('adddate')
		  if date_format:
		    item_dict['adddate'] = str(date_format)
		  
		  json_append.append(item_dict)
		return qry



app = webapp2.WSGIApplication([
    ('/', Home),
    ('/about', About),
], debug=True)
