package business{
	
	
	public class TeamManager{
		
	/*** EXPORT ***/
		[Bindable] public var teamListData:Object;
		
		public function TeamManager(){
			
		}
		
		public function updateList(result:Object):void{
			teamListData = result.teams;
			
		}

	}
}