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
		
		public var stackIndex:int;
		public var whichList:String;
		
		public var name:String;
		public var code:String;
		
		public var firstName:String;
		public var lastName:String;
		public var city:String;
		public var country:String;
		public var tournament:String;
		public var division:String;
		public var dateString:String;
		public var key:String;
		
		
		public function UIEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
	}
}