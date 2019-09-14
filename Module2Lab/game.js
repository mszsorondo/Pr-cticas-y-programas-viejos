var secret = Math.round(Math.random()*10);
console.log(secret);
var answers = [];
var i = 1;
var check = false;

var runGame = function()
{
	while (i < 6)
{
	var tries = parseInt(prompt("Guess the number (opportunity " + i + " of 5"));
	if (tries == secret)
	{
		alert("Congratulations! You have guessed the number :)");
		break;
	}	
	else if (typeof(tries) !== typeof(secret))
	{
		alert("You can´t use datatypes that aren´t numbers. Please try again.")
		tries = prompt("Guess the number (opportunity " + i + " of 5");
	}
	else if (tries != secret)
	{
		checkifrepeats();	
	}



	
}
}


var checkifrepeats = function()
{
		answers.push(tries);
		console.log(tries);
		for (k of answers)
		{
				if (k==tries)
				{
					check=true;
				}
		}
		if (i != 5 && check==false)
		{
					alert("You didn´t guess it... Try again!");
					i++;

		}
		
		else if (i != 5 && check==true)
		{
			alert("You can´t repeat an answer! Try again.");
			runGame();
		}
		else
		{
			alert("You lost!");
		}	
}
runGame();

//this function checks if the number is already in the answers list
