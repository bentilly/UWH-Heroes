package events
{
	import flash.events.Event;

	public class UIEvent extends Event
	{
		
		public static const SWITCH_STACK:String = "switchStackEvent";
		public static const GET_LIST:String = "getListEvent";
		
		public static const ADD_ITEM_TO_LIST:String = "addItemToListEvent";
		public static const ADD_PERSON:String = "addPersonEvent";
		public static const FIND_PERSON:String = "findPersonEvent";
		public static const SAVE_PERSON:String = "savePersonEvent";
		
		public static const ADD_TOURNAMENT:String = "addTournamentEvent";
		public static const FIND_TOURNAMENT:String = "findTournamentEvent";
		public static const SAVE_TOURNAMENT:String = "saveTournamentEvent";
		
		public static const ADD_TEAM:String = "addTeamEvent";
		public static const GET_TEAMS:String = "getTeamsEvent";
		public static const GET_TEAM_PLAYERS:String = "getTeamPlayersEvent";
		public static const SAVE_TEAM_PLAYER:String = "saveTeamPlayerEvent";
		public static const SAVE_TEAM_OFFICIAL:String = "saveTeamOfficialEvent";
		public static const ADD_PERSON_TO_TEAM:String = "addPersonToTeamEvent";
		public static const ADD_COACH_TO_TEAM:String = "addCoachToTeamEvent";
		public static const ADD_OFFICIAL_TO_TEAM:String = "addOfficialToTeamEvent";
		
		public static const RESET_PAGES:String = "resetPagesEvent";
		
	// GAMES
		public static const SELECT_TOURNEY:String = "selectTourneyEvent";
		public static const GET_TEAMS_FOR_TOURNEY:String = "getTeamsForTourneyEvent";
		public static const NEW_GAME:String = "newGameEvent";
		
		
		public var key:String;
		public var personKey:String;
		public var teamKey:String;
		public var positionKey:String;
		public var rankKey:String;
		public var tournamentKey:String;
		public var divisionKey:String;
		public var countryKey:String;
		
		
		public var stackIndex:int;
		public var whichList:String;
		
		public var name:String;
		public var code:String;
		public var title:String;
		
		public var firstName:String;
		public var lastName:String;
		public var city:String;
		public var country:String;
		public var tournament:String;
		public var division:String;
		public var dateString:String;
		
		public var team:String;
		
		//Games
		public var gameDate:String;
		public var gameDivision:String;
		public var gameType:String;
		public var testMatch:Boolean;
		public var bscore:Number;
		public var bCountry:String;
		public var bDivision:String;
		public var wscore:Number;
		public var wCountry:String;
		public var wDivision:String;
		
		
		
		
		public function UIEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
	}
}