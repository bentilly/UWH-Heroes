import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db

from python.data import *

class FindPerson(webapp.RequestHandler):
	def get(self):
		fn = self.request.get('firstName')
		ln = self.request.get('lastName')
		
		if ln == "":
			people = db.GqlQuery("SELECT * FROM Person WHERE firstName >= :1 AND firstName < :2", fn, fn+u'\ufffd').fetch(1000)
		else:
			people = db.GqlQuery("SELECT * FROM Person WHERE lastName >= :1 AND lastName < :2", ln, ln+u'\ufffd').fetch(1000)
				
		template_values = {
							"people":people
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/person.xml')
		self.response.out.write(template.render(path, template_values))
			
			
class AddPerson(webapp.RequestHandler):
	def post(self):
		p = Person()
		p.firstName = self.request.get('firstName')
		p.lastName = self.request.get('lastName')
		p.put()
		
		people = db.GqlQuery("SELECT * FROM Person ORDER BY lastName").fetch(1000)
		template_values = {
							"people":people
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/person.xml')
		self.response.out.write(template.render(path, template_values))
		
class SavePerson(webapp.RequestHandler):
	def post(self):
		k = db.Key(self.request.get('key'))
		p = db.get(k)
		p.firstName = self.request.get('firstName')
		p.lastName = self.request.get('lastName')
		p.put()
		
		people = db.GqlQuery("SELECT * FROM Person ORDER BY lastName").fetch(1000)
		template_values = {
							"people":people
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/person.xml')
		self.response.out.write(template.render(path, template_values))

