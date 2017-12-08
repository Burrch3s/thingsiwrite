# thingsiwrite
Scripts and programs I've written for classwork or to make life easier

Classwork directory: 
	branchpred.py- Script for an assignment that accepted a file 
	of unknown size containing hex addresses, an '@' or '.' symbol
	then another hex address on every line. This was to, in a very 
	basic way, simulate different algorithms that exist for 
	predicting if branches were to be taken or not.

	hw_addition.asm- an assembly program that is targetted towards
	a turing machine architecture that confer wrote an supplied
	for the class. The architectures assembly syntax and opcodes
	were implemented and fine tuned by confer, but developed by
	the whole class, which was interesting. This particular program
	took 2 numbers and added them together.

	hwfinal.asm- an assembly program that is targetted towards the
	sunyat architecture that confer and a group of students developed.
	This particular program takes in 2 digits and converts them to the
	hex equivalent. (ex. 15 turns to 0x0F)

Openhouse directory:
	basic-netcat.py- Script from BlackHatPython that emulates
	functionality of netcat.

	basic-sshRcmd.py- Script from BlackHatPython that establishes
	or listens for a connection and emulates ssh. Provides encrypted
	connection as the listener and works with basic-sshserver.py

	basic-sshserver.py- Script from BlackHatPython that allows for
	encrypted connection. Emulates ssh and acts as the client/sender
	for the connection. Works with basic-sshRcmd.py

	basic-ssh-connection.py- Script from BlackHatPython that uses
	default creds to establish ssh connection that sends a single
	command 'ls'

	tcp-client.py- Script from BlackHatPython that establishes basic
	tcp connection to google and posts the response from a GET 
	request to the terminal

redteam directory:
	will be adding more to this, essentially it was ideas/lil scripts
	that I was planning to use in cnyhackathon to be a troll

	troll.sh- script that will not only write in ascii art, 
	"redteam rules" to the terminal, but will also utilize tput to
	move the terminals cursor back up to the beginning of the ascii
	art, essentially forcing users to write over the ascii art or
	repeatedly clear the screen until they delete the cronjob invoking
	this script. lolz
