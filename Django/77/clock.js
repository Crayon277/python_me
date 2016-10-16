var words = document.getElementById("ctimeline");
var cwords = words.getContext("2d");
cwords.font = "30px Arial";
cwords.fillText("Hello World",5,25);


function test_method(fname,lname){
	document.getElementById("test").innerHTML = "I love "+ fname + " " + lname;
}	

function test(){
	person = new Object();
	person.name = "Xu qiqi";
	var firstname = prompt("What's your first name?");
	while(!firstname){
		alert("Please Enter your name");
		firstname = prompt("What's your first name?");
	}
	var lastname = prompt("What's your last name?");
	while(!lastname){
		alert("Please Enter your last name");
		lastname = prompt("What's your last name?");
	}
	test_method(firstname,lastname);
	words_set();
}


function clock_set(){
	var time_clock = new Date();
	time_clock.setFullYear(2012,06,23);
	time_clock.setHours(0);
	time_clock.setMinutes(0);
	time_clock.setSeconds(0);
	time_clock.setMilliseconds(0);

}


