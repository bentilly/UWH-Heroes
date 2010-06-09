package business{
	import mx.controls.Alert;
	
	
	
	public class TeamManager{
		
	/*** EXPORT ***/
		[Bindable] public var teamListData:Object;
		[Bindable] public var teamPlayersListData:Object;
		[Bindable] public var teamOfficialsListData:Object;
		[Bindable] public var teamCoachData:Object;
		
		
		public function TeamManager(){
			
		}
		
		public function updateList(result:Object):void{
			teamListData = result.teams;
			trace("Got Teams");
			
		}

		public function updateCurrentTeamList(result:Object):void{
			if(result.response == "player already in team"){
				Alert.show("Player already in team");
			}
			teamPlayersListData = result.team.teamPlayers;
			teamCoachData = result.team.teamCoach;
			teamOfficialsListData = result.team.teamOfficials;
		}

	}
}