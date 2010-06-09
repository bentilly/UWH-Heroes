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
		
class GetTeams(webapp.RequestHandler):
	def get(self):
		teams = db.GqlQuery("SELECT * FROM Team").fetch(1000)
		
		template_values = {
							"teams":teams
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/team.xml')
		self.response.out.write(template.render(path, template_values))

class GetTeamPlayers(webapp.RequestHandler):
	def get(self):
		tk = db.Key(self.request.get('teamKey'))
		team = db.get(tk)
		
		players = team.teamPlayers_set
		coach = team.coach
		officials = team.teamOfficials_set
		
		template_values = {
							"players":players,
							"coach":coach,
							"officials":officials
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/teamPlayers.xml')
		self.response.out.write(template.render(path, template_values))		

class AddPersonToTeam(webapp.RequestHandler):
	def post(self):
		tk = db.Key(self.request.get('teamKey'))
		team = db.get(tk)
		pk = db.Key(self.request.get('personKey'))
		person = db.get(pk)
		
		addPlayer = True
		
		if team.teamPlayers_set.count() > 0:
			for p in team.teamPlayers_set:
				if p.person.key() == person.key():
					addPlayer = False
					
		
		if addPlayer:
			pos = db.GqlQuery("SELECT * FROM Position WHERE name = 'Player'").get()
			rnk = db.GqlQuery("SELECT * FROM Rank WHERE name = 'Player'").get()
			tp = Team_Player()
			tp.person = person
			tp.team = team
			tp.position = pos
			tp.rank = rnk
			tp.put()
			self.response.out.write("<response>success</response>")
		else:
			self.response.out.write("<response>player already in team</response>")
			
		self.redirect('/getTeamPlayers?teamKey=%s' % tk)


class AddCoachToTeam(webapp.RequestHandler):
	def post(self):
		tk = db.Key(self.request.get('teamKey'))
		team = db.get(tk)
		pk = db.Key(self.request.get('personKey'))
		person = db.get(pk)
		
		team.coach = person
		team.put()

		players = team.teamPlayers_set
		coach = team.coach
		officials = team.teamOfficials_set
		
		template_values = {
							"players":players,
							"coach":coach,
							"officials":officials
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/teamPlayers.xml')
		self.response.out.write(template.render(path, template_values))

		
		
class SaveTeamPlayer(webapp.RequestHandler):
	def post(self):	
		tpk = db.Key(self.request.get('key'))
		teamPlayer = db.get(tpk)
		teamPlayer.position = db.Key(self.request.get('positionKey'))
		teamPlayer.rank = db.Key(self.request.get('rankKey'))
		teamPlayer.put()
		
		team = teamPlayer.team
		
		players = team.teamPlayers_set
		coach = team.coach
		officials = team.teamOfficials_set
		
		template_values = {
							"players":players,
							"coach":coach,
							"officials":officials
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/teamPlayers.xml')
		self.response.out.write(template.render(path, template_values))

class AddOfficialToTeam(webapp.RequestHandler):
	def post(self):
		tk = db.Key(self.request.get('teamKey'))
		team = db.get(tk)
		pk = db.Key(self.request.get('personKey'))
		person = db.get(pk)
		
		addOfficial = True
		
		if team.teamOfficials_set.count() > 0:
			for o in team.teamOfficials_set:
				if o.person.key() == person.key():
					addOfficial = False
					
		
		if addOfficial:
			to = Team_Official()
			to.person = person
			to.team = team
			to.put()
			self.response.out.write("<response>success</response>")
		else:
			self.response.out.write("<response>player already in team</response>")

		players = team.teamPlayers_set
		coach = team.coach
		officials = team.teamOfficials_set
		
		template_values = {
							"players":players,
							"coach":coach,
							"officials":officials
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/teamPlayers.xml')
		self.response.out.write(template.render(path, template_values))
		
class SaveTeamOfficial(webapp.RequestHandler):
	def post(self):	
		tok = db.Key(self.request.get('key'))
		teamOfficial = db.get(tok)
		teamOfficial.title = self.request.get('title')
		teamOfficial.put()
		
		team = teamOfficial.team
		
		players = team.teamPlayers_set
		coach = team.coach
		officials = team.teamOfficials_set
		
		template_values = {
							"players":players,
							"coach":coach,
							"officials":officials
							}
		path = os.path.join(os.path.dirname(__file__), '../xml/lists/teamPlayers.xml')
		self.response.out.write(template.render(path, template_values))
		
		
		
		
		
		