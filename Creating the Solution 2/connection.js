var year = ['1900','1930','1950','1970', '2000', '2016'];
	var power = [16.67,130.56,333.33,1174.56,2654.95,4036.07];
	function clicked(){
		console.log("Searching...")
		var value = document.getElementById("searchbar3").value;

		for (i = 0; i < year.length; i++){
			if (year[i] === value){
				document.getElementById("results3").innerHTML = "The global hydroelectric consumption"+ " " + year[i] + " " + "was" + " " + power[i] + " " + "terawatts.";
				return;
				}
			}
		document.getElementById("results3").innerHTML = "There is no data for this year at the moment. Years with data are: 1900, 1930, 1950, 1970, 2000, and 2016";
	}