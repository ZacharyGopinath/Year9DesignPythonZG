var countries = ["Canada","US","Germany","France", "Japan"]
var year = [2015, 2015, 2015, 2015]
var eperc = [7,353,510,732]


document.getElementById("searchbutton").onclick = clicked;

function clicked() {
	console.log("CLICKED");

	
	var value = document.getElementById("searchbar").value
	
	for (i = 0; i < countries.length; i = i + 1) {

		if (countries[i] === value) {
		
			document.getElementById("results").innerHTML = value+" used "+eperc[i] + " kilowatts of power" + " in the year " + year[i] + ".";
	
			return; 
		}

	}

	document.getElementById("results").innerHTML = "There is no data for this country at the moment. Countries with data are: Canada, US, Germany, France, and Japan";
	
}