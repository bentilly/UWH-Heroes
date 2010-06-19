package business{
	import events.UIEvent;
	
	
	
	public class GameManager{
		
		[Bindable] public var gamesListData:Object;
		[Bindable] public var tournamentTitle:Object;
		[Bindable] public var tournamentKey:String;
		[Bindable] public var blackTeamListData:Object;
		[Bindable] public var whiteTeamListData:Object;
		
		public function GameManager(){
			
		}
		public function updateGameList(result:Object):void{
			gamesListData = result.games;
			tournamentTitle = result.tournament.name;
			tournamentKey = result.tournament.key;
		}
		public function updateTourneyTeamList(result:Object, event:UIEvent):void{
			
			if(event.team == "black"){
				blackTeamListData = result.teams;
			}else{
				whiteTeamListData = result.teams;
			}
		}
		public function newGameResponse(result:Object, event:UIEvent):void{
			trace("_________________");
			trace(result.response);
			trace("_________________");
		}

	}
}