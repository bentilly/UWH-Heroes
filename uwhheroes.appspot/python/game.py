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

class NewGame(webapp.RequestHandler):
	def post(self):
		game = Game()
		game.tournament = db.Key(self.request.get('tournamentKey'))
		dateString = self.request.get('gameDate')
		game.startDate = datetime.datetime.strptime(dateString, '%d-%m-%Y').date()
		game.division = db.Key(self.request.get('gameDivision'))
		game.gameType = db.Key(self.request.get('gameType'))
		if self.request.get('testMatch') == 'true':
			game.testMatch = True
		else:
			game.testMatch = False
		game.put()
		
		#Process Black Team
		bCountry = db.Key(self.request.get('bCountry'))
		bDivision = db.Key(self.request.get('bDivision'))
		bTeams = db.GqlQuery("SELECT * FROM Team WHERE tournament = :1 AND division = :2 AND country = :3", game.tournament, bDivision, bCountry)
		if bTeams.count() > 1:
			#ask which team
			self.response.out.write('<response>More than one black team</response>')
		elif bTeams.count() > 0:
			#one team
			bgt = GameTeam()
			bgt.team = bTeams.get()
			bgt.score = int(self.request.get('bscore'))
			bgt.colour = 'black'
			bgt.game = game
			bgt.put()

		else:
			#no team
			bt = Team()
			bt.country = bCountry
			bt.tournament = game.tournament
			bt.division = bDivision
			bt.put()
			
			bgt = GameTeam()
			bgt.team = bTeams.get()
			bgt.score = int(self.request.get('bscore'))
			bgt.colour = 'black'
			bgt.game = game
			bgt.put()

		
		#Process White Team
		wCountry = db.Key(self.request.get('wCountry'))
		wDivision = db.Key(self.request.get('wDivision'))
		wTeams = db.GqlQuery("SELECT * FROM Team WHERE tournament = :1 AND division = :2 AND country = :3", game.tournament, wDivision, wCountry)
		if wTeams.count() > 1:
			self.response.out.write('<response>More than one white team</response>')
		elif wTeams.count() > 0:
			#one team
			wgt = GameTeam()
			wgt.team = wTeams.get()
			wgt.score = int(self.request.get('wscore'))
			wgt.colour = 'white'
			wgt.game = game
			wgt.put()
		else:
			#no team
			wt = Team()
			wt.country = wCountry
			wt.tournament = game.tournament
			wt.division = wDivision
			wt.put()
			
			wgt = GameTeam()
			wgt.team = wTeams.get()
			wgt.score = int(self.request.get('wscore'))
			wgt.colour = 'white'
			wgt.game = game
			wgt.put()
		
		self.response.out.write('<response>Made it to here</response>')












