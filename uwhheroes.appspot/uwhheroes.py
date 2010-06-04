import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db

from python.data import *
from python.lists import *
from python.person import *
from python.tournament import *
from python.team import *

class Main(webapp.RequestHandler):
    def get(self):
		self.response.out.write("UWH Heroes")


application = webapp.WSGIApplication([
                                     ('/', Main),
                                     #Lists
                                     ('/getList', GetList),
                                     ('/addToList', AddToList),
                                     #Person
                                     ('/addPerson', AddPerson),
                                     ('/findPerson', FindPerson),
                                     ('/savePerson', SavePerson),
                                     #Tournament
                                     ('/addTournament', AddTournament),
                                     ('/findTournament', FindTournament),
                                     ('/saveTournament', SaveTournament),
                                     #Team
                                     ('/addTeam', AddTeam),
                                     
                                     
                                     
                                     ], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()