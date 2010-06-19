from google.appengine.ext import db

#-----------List

class Division(db.Model):
	name = db.StringProperty()
	code = db.StringProperty()

class Country(db.Model):
	name = db.StringProperty()
	code = db.StringProperty()

class GameType(db.Model):
	name = db.StringProperty()
	code = db.StringProperty()
	
class Position(db.Model):
	name = db.StringProperty()
	code = db.StringProperty()
	
class Rank(db.Model):
	name = db.StringProperty()
	code = db.StringProperty()
	

	
#----------- People

class Person(db.Model):
	firstName = db.StringProperty()
	lastName = db.StringProperty()


#----------- Objects

class Tournament(db.Model):
	country = db.ReferenceProperty(Country)
	city = db.StringProperty()
	startDate = db.DateProperty()
	name = db.StringProperty()

class Team(db.Model):
	division = db.ReferenceProperty(Division)
	tournament = db.ReferenceProperty(Tournament)
	country = db.ReferenceProperty(Country)
	name = db.StringProperty()
	coach = db.ReferenceProperty(Person)
	
class Game(db.Model):
	tournament = db.ReferenceProperty(Tournament, collection_name='game_set')
	division = db.ReferenceProperty(Division)
	gameType = db.ReferenceProperty(GameType)
	startDate = db.DateProperty()
	testMatch = db.BooleanProperty()
	
class GameTeam(db.Model):
	team = db.ReferenceProperty(Team)
	score = db.IntegerProperty()
	colour = db.StringProperty()
	game = db.ReferenceProperty(Game, collection_name='gameTeam_set')


#------------References

class Game_Player(db.Model):
	person = db.ReferenceProperty(Person)
	gameTeam = db.ReferenceProperty(GameTeam)
	position = db.ReferenceProperty(Position)
	rank = db.ReferenceProperty(Rank)
	
class Game_Coach(db.Model):
	person = db.ReferenceProperty(Person)
	gameTeam = db.ReferenceProperty(GameTeam)

class Team_Player(db.Model):
	person = db.ReferenceProperty(Person)
	team = db.ReferenceProperty(Team, collection_name='teamPlayers_set')
	position = db.ReferenceProperty(Position)
	rank = db.ReferenceProperty(Rank)

class Team_Official(db.Model):
	person = db.ReferenceProperty(Person)
	team = db.ReferenceProperty(Team, collection_name='teamOfficials_set')
	title = db.StringProperty()
	












