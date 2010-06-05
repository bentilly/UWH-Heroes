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

class Squad(db.Model):
	country = db.ReferenceProperty(Country)
	tournament = db.ReferenceProperty(Tournament)

class Team(db.Model):
	division = db.ReferenceProperty(Division)
	tournament = db.ReferenceProperty(Tournament)
	country = db.ReferenceProperty(Country)
	name = db.StringProperty()
	#def players = ref via Team_Player

class GameTeam(db.Model):
	team = db.ReferenceProperty(Team)
	#coach = db.ReferenceProperty(Coach)
	score = db.IntegerProperty()
	#def players = ref via Game_Player
	
class Game(db.Model):
	tournament = db.ReferenceProperty(Tournament)
	division = db.ReferenceProperty(Division)
	gameType = db.ReferenceProperty(GameType)
	startDateTime = db.DateTimeProperty()
	blackTeam = db.ReferenceProperty(GameTeam, collection_name="whiteTeam_set")
	whiteTeam = db.ReferenceProperty(GameTeam)
	testMatch = db.BooleanProperty()
	#def referees = ref via Game_Referee
	


#------------References

class Game_Player(db.Model):
	person = db.ReferenceProperty(Person)
	gameTeam = db.ReferenceProperty(GameTeam)
	position = db.ReferenceProperty(Position)
	rank = db.ReferenceProperty(Rank)
	
class Game_Coach(db.Model):
	person = db.ReferenceProperty(Person)
	gameTeam = db.ReferenceProperty(GameTeam)

class Game_Referee(db.Model):
	person = db.ReferenceProperty(Person)
	game = db.ReferenceProperty(Game)

class Team_Player(db.Model):
	person = db.ReferenceProperty(Person)
	team = db.ReferenceProperty(Team)
	position = db.ReferenceProperty(Position)
	rank = db.ReferenceProperty(Rank)
	
class Team_Coach(db.Model):
	person = db.ReferenceProperty(Person)
	team = db.ReferenceProperty(Team)

class Team_Official(db.Model):
	person = db.ReferenceProperty(Person)
	team = db.ReferenceProperty(Team)
	title = db.StringProperty()

class Squad_Official(db.Model):
	person = db.ReferenceProperty(Person)
	squad = db.ReferenceProperty(Squad)
	title = db.StringProperty()

class Tournament_Official(db.Model):
	person = db.ReferenceProperty(Person)
	tournament = db.ReferenceProperty(Tournament)
	title = db.StringProperty()
	












