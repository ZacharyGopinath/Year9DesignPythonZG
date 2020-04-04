var countries = ["Canada","US","Germany","France", "Japan"];
	var eperc = [88431,79056,44390,42909,39874];
	function clicked(){
		var value = document.getElementById("searchbar").value;
		for (i = 0; i < countries.length; i++){
			if (countries[i] === value){
				document.getElementById("results").innerHTML = "The average energy consumption in"+ " " + countries[i] + " " + "is" + " " + eperc[i]+ " " + "kilowatts.";
				
				return;
				}
			}
		document.getElementById("results").innerHTML = "There is no data for this country at the moment. Countries with data are: Canada, US, Germany, France, and Japan";
	}