# thingsiwrite
Scripts and programs I've written for classwork or to make life easier

branchpred.py- Script for an assignment that accepted a file of unknown size containing hex addresses, an '@' or '.' symbol then another hex address on every line. This was to, in a very basic way, simulate different algorithms that exist for predicting if branches were to be taken or not.

basic-netcat.py- Script from BlackHatPython that emulates functionality of netcat.

basic-sshRcmd.py- Script from BlackHatPython that establishes/listens for a connection and emulates ssh. Provides encrypted connection as the listener and works with basic-sshserver.py

basic-sshserver.py- Script from BlackHatPython that allows for encrypted connection. Emulates ssh and acts as the client/sender for the connection. Works with basic-sshRcmd.py

basic-ssh-connection.py- Script from BlackHatPython that uses default creds to establish ssh connection that sends a single command 'ls'

tcp-client.py- Script from BlackHatPython that establishes basic tcp connection to google and posts the response from a GET request to the terminal
