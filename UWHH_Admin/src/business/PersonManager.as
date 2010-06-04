package business{
	
	public class PersonManager{
		
	/*** EXPORT ***/
		[Bindable] public var personListData:Object;
		
		public function PersonManager(){
			
		}
		
		public function updateList(result:Object):void{
			personListData = result.people;
			trace("::::UPDATE people");
		}

	}
}