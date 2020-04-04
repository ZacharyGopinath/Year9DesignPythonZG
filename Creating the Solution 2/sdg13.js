var year = ['1900','1930','1950','1970', '2000', '2016'];
	var temp = [-0.20,-0.14,-0.07,-0.03,0.29, 0.80];
	function clicked(){
		console.log("Searching...")
		var value = document.getElementById("searchbar2").value;

		for (i = 0; i < year.length; i++){
			if (year[i] === value){
				document.getElementById("results2").innerHTML = "The average global temperature in"+ " " + year[i] + " " + "was" + " " + temp[i] + " " + "degrees celcius.";
				return;
				}
			}
		document.getElementById("results2").innerHTML = "There is no data for this year at the moment. Years with data are: 1900, 1930, 1950, 1970, 2000, and 2016";
	}