#TODO:  Add / Remove multiple items in the same command
#       Change location of the todo.txt file
#		Archive all done tasks into a separate done.txt file
#~ 
#~ USAGE: python todo.py <action> <text>
#~ <action> can be either 'add' , 'done' or 'list'
#~ <text> need not be provided as an argument. If it is skipped, the program will prompt the user for the appropriate input

import sys,re
def main():
	#~ Declare the important variables
	try:
		action=sys.argv[1]
	except IndexError:
		action=raw_input("Pleae enter an option - \n- add\n- done\n- list\n Enter your option: ")
	
	print action
	hashtags=[]
	#~ Read the contents of the current file and store it in the dict
	task_dict=read()
	
	for a in task_dict.values():
		if a[1] != ' ': hashtags.append(a[1])

	#~ Avoid dupicate entried by converting the list to a set and then back to a list
	hashtag=list(set(hashtags))
	
	if len(sys.argv) == 2 and action=='add':
		text=raw_input("Please enter the task to be added : ")+'\n'
	elif len(sys.argv) == 2 and action=='done':
		text=raw_input("Please enter the s.no. of the completed task : ")+'\n'
	elif len(sys.argv) == 2 and action=='list':
		print 'Please enter one of the following: '
		for h in hashtag:
			print '- '+h
		text=raw_input('- '+'All (default) : \n Enter your choice: ')
				
	if len(sys.argv) > 2:
		text=sys.argv[2]+'\n'
	else:
		if action=='list': text='All'
			
	if action=='add':
		#~ print task_dict, task_dict.items(), len(task_dict.items())
		for i in xrange(1,len(task_dict.items())+2):
			if not task_dict.has_key(str(i)):
				try:
					m=re.search(r'(.+) #(.+)',text)
					task_dict[str(i)]=[m.group(1),m.group(2)]
				except AttributeError:
					m=re.search(r'(.+)',text)
					task_dict[str(i)]=[m.group(1),' ']
					break
		write(task_dict)
		print "\nNew task has been added\n"
		#~ print task_dict
	elif action=='done':
			task_dict.pop(str(text)[0])
			write(task_dict)
			print "\nTask number "+text[0]+' has been successfully removed\n'
	elif action=='list':
		if text == '' or text == 'All' : display('all')
		else:
			display(text)
	else:
			print "\""+action+"\""+ " is not a recognized command. Please use one of these options:\n- add\n- done\n- list\n"


def read():
	try:
		todo=open("todo.txt")
		tasks=todo.readlines()
		todo.close()
		#~ print "I have entered try"
		task_dict={}
		for t in tasks:
			try:
				m=re.search(r'(\d+)\. (.+) #(.+)',t)
				task_dict[m.group(1)]=[m.group(2),m.group(3)]
			except AttributeError:
				m=re.search(r'(\d+)\. (.+)',t)
				task_dict[m.group(1)]=[m.group(2),' ']
		return task_dict	
	except IOError:
		todo=open("todo.txt","w")
		print "File does not exist. New file has been created"
		todo.close()
		return {}


def write (task_dict):
	f=open("todo.txt","w")
	for a,b in sorted(task_dict.iteritems()):
		if b[1]!=' ':
			f.write(a+'. '+b[0]+' #'+b[1]+'\n')
		else:
			f.write(a+'. '+b[0]+'\n')
	#~ for a,b in sorted(task_dict.iteritems()):
		#~ f.write(str(a)+'. '+b)
	f.close()
	display('all')

	
def display(text):
	print '\n'+20*'*'+'\nTO-DO LIST\n'+20*'*'
	f=open("todo.txt")
	tasks=f.readlines()
	f.close()
	for t in tasks:
		if text=='all':
			print t,
		else:
			if text in t:
				print t,
	print '\n'	

if __name__=='__main__':
	main()
