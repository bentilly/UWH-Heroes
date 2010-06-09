import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db
import datetime

from python.data import *


class GetGamesForTourney(webapp.RequestHandler):
	def post(self):
		tk = db.Key(self.request.get('tournamentKey'))
		tournament = db.get(tk)
		
		template_values = {
							"tournament":tournament
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/game.xml')
		self.response.out.write(template.render(path, template_values))
		
		
class GetTeamsForTourney(webapp.RequestHandler):
	def post(self):
		tk = db.Key(self.request.get('tournamentKey'))
		dk = db.Key(self.request.get('divisionKey'))
		ck = db.Key(self.request.get('countryKey'))
		teams = db.GqlQuery("SELECT * FROM Team WHERE tournament = :1 AND division = :2 AND country = :3", tk, dk, ck)
		template_values = {
							"teams":teams
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/team.xml')
		self.response.out.write(template.render(path, template_values))