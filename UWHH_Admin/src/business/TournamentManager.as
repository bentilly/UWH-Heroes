package business{
	import mx.collections.ArrayCollection;
	
	
	public class TournamentManager{
		
	/*** EXPORT ***/
		[Bindable] public var tournamentListData:Array;
	
		public function TournamentManager(){
			
		}
		
		public function updateList(result:Object):void{
			trace(":::::::::::::::::::::::: Update tournament list");
			tournamentListData = new Array();
			try{
				for each( var t:Object in result.tournaments.tournament){
					var dateBits:Array = t.date.split("-");
					t.dateObject = new Date(dateBits[2], dateBits[1]-1, dateBits[0]);
					t.year = dateBits[2]
					tournamentListData.push(t)
				}
				tournamentListData.sortOn("year", Array.DESCENDING);
			}catch(e:Error){
			}
		}

	}
}