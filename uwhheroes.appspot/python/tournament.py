import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db
import datetime

from python.data import *

class FindTournament(webapp.RequestHandler):
	def get(self):
		n = self.request.get('name')
		c = self.request.get('city')
		
		if c == "":
			tournaments = db.GqlQuery("SELECT * FROM Tournament WHERE name >= :1 AND name < :2", n, n+u'\ufffd').fetch(1000)
		else:
			tournaments = db.GqlQuery("SELECT * FROM Tournament WHERE city >= :1 AND city < :2", c, c+u'\ufffd').fetch(1000)
				
		template_values = {
							"tournaments":tournaments
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/tournament.xml')
		self.response.out.write(template.render(path, template_values))
			
			
class AddTournament(webapp.RequestHandler):
	def post(self):
		t = Tournament()
		t.name = self.request.get('name')
		t.city = self.request.get('city')
		t.country = db.Key(self.request.get('country'))
		dateString = self.request.get('date')
		t.startDate = datetime.datetime.strptime(dateString, '%d-%m-%Y').date()
		t.put()
		
		tournaments = db.GqlQuery("SELECT * FROM Tournament ORDER BY startDate").fetch(1000)
		template_values = {
							"tournaments":tournaments
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/tournament.xml')
		self.response.out.write(template.render(path, template_values))
		
class SaveTournament(webapp.RequestHandler):
	def post(self):
		k = db.Key(self.request.get('key'))
		t = db.get(k)
		t.name = self.request.get('name')
		t.city = self.request.get('city')
		t.country = db.Key(self.request.get('country'))
		dateString = self.request.get('date')
		t.startDate = datetime.datetime.strptime(dateString, '%d-%m-%Y').date()
		t.put()
		
		tournaments = db.GqlQuery("SELECT * FROM Tournament ORDER BY startDate").fetch(1000)
		template_values = {
							"tournaments":tournaments
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/tournament.xml')
		self.response.out.write(template.render(path, template_values))

