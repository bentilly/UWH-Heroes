package business{
	import events.UIEvent;
	
	public class ListsManager{
		
	/*** EXPORT ***/
		[Bindable] public var divisionListData:Object;
		[Bindable] public var countryListData:Object;
		[Bindable] public var positionListData:Object;
		[Bindable] public var gameTypeListData:Object;
		[Bindable] public var rankListData:Object;
		
		
		public function ListsManager(){
			
		}
		
		public function updateList(result:Object, event:UIEvent):void{
			trace("got list");
			switch(event.whichList){
				case "division":
					divisionListData = result.items;
					break;
				case "country":
					countryListData = result.items;
					break;
				case "position":
					positionListData = result.items;
					break;
				case "gameType":
					gameTypeListData = result.items;
					break;
				case "rank":
					rankListData = result.items;
					break;
				default:
					break;
			}
		}
		

	}
}