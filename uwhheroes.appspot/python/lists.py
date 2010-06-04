import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db

from python.data import *


class GetList(webapp.RequestHandler):
	def get(self):
		listName = self.request.get('whichList')
		if listName == "division":
			items = db.GqlQuery("SELECT * FROM Division ORDER BY name").fetch(1000)
			template_values = {
								"items":items
								}
			path = os.path.join(os.path.dirname(__file__), '../xml/lists/list.xml')
			self.response.out.write(template.render(path, template_values))
			
		elif listName == "country":
			items = db.GqlQuery("SELECT * FROM Country ORDER BY name").fetch(1000)
			template_values = {
								"items":items
								}
			path = os.path.join(os.path.dirname(__file__), '../xml/lists/list.xml')
			self.response.out.write(template.render(path, template_values))
			
		elif listName == "position":
			items = db.GqlQuery("SELECT * FROM Position ORDER BY name").fetch(1000)
			template_values = {
								"items":items
								}
			path = os.path.join(os.path.dirname(__file__), '../xml/lists/list.xml')
			self.response.out.write(template.render(path, template_values))
			
		elif listName == "gameType":
			items = db.GqlQuery("SELECT * FROM GameType ORDER BY name").fetch(1000)
			template_values = {
								"items":items
								}
			path = os.path.join(os.path.dirname(__file__), '../xml/lists/list.xml')
			self.response.out.write(template.render(path, template_values))
			
		elif listName == "rank":
			items = db.GqlQuery("SELECT * FROM Rank ORDER BY name").fetch(1000)
			template_values = {
								"items":items
								}
			path = os.path.join(os.path.dirname(__file__), '../xml/lists/list.xml')
			self.response.out.write(template.render(path, template_values))







class AddToList(webapp.RequestHandler):
	def post(self):
		listName = self.request.get('whichList')
		if listName == "division":
			i = Division()
			i.name = self.request.get('name')
			i.code = self.request.get('code')
			i.put()
			
			items = db.GqlQuery("SELECT * FROM Division ORDER BY name").fetch(1000)
			template_values = {
								"items":items
								}
			path = os.path.join(os.path.dirname(__file__), '../xml/lists/list.xml')
			self.response.out.write(template.render(path, template_values))
			
		elif listName == "country":
			i = Country()
			i.name = self.request.get('name')
			i.code = self.request.get('code')
			i.put()
			
			items = db.GqlQuery("SELECT * FROM Country ORDER BY name").fetch(1000)
			template_values = {
								"items":items
								}
			path = os.path.join(os.path.dirname(__file__), '../xml/lists/list.xml')
			self.response.out.write(template.render(path, template_values))
			
		elif listName == "position":
			i = Position()
			i.name = self.request.get('name')
			i.code = self.request.get('code')
			i.put()
			
			items = db.GqlQuery("SELECT * FROM Position ORDER BY name").fetch(1000)
			template_values = {
								"items":items
								}
			path = os.path.join(os.path.dirname(__file__), '../xml/lists/list.xml')
			self.response.out.write(template.render(path, template_values))
			
		elif listName == "gameType":
			i = GameType()
			i.name = self.request.get('name')
			i.code = self.request.get('code')
			i.put()
			
			items = db.GqlQuery("SELECT * FROM GameType ORDER BY name").fetch(1000)
			template_values = {
								"items":items
								}
			path = os.path.join(os.path.dirname(__file__), '../xml/lists/list.xml')
			self.response.out.write(template.render(path, template_values))
			
		elif listName == "rank":
			i = Rank()
			i.name = self.request.get('name')
			i.code = self.request.get('code')
			i.put()
			
			items = db.GqlQuery("SELECT * FROM Rank ORDER BY name").fetch(1000)
			template_values = {
								"items":items
								}
			path = os.path.join(os.path.dirname(__file__), '../xml/lists/list.xml')
			self.response.out.write(template.render(path, template_values))




















