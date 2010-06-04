import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db
import datetime

from python.data import *


class AddTeam(webapp.RequestHandler):
	def post(self):
		t = Team()
		t.name = self.request.get('name')
		t.country = db.Key(self.request.get('country'))
		t.tournament = db.Key(self.request.get('tournament'))
		t.division = db.Key(self.request.get('division'))
		t.put()
		
		teams = db.GqlQuery("SELECT * FROM Team").fetch(1000)
		
		template_values = {
							"teams":teams
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/team.xml')
		self.response.out.write(template.render(path, template_values))