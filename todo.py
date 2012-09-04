#TODO:  Add / Remove multiple items in the same command
#       Change location of the todo.txt file
#       Add support for multiple lists using #hashtags
#		Archive all done tasks into a separate done.txt file

import sys,re
def main():
	#~ Declare the important variables
	action=sys.argv[1]
	if len(sys.argv) == 2 and action=='add':
		text=raw_input("Please enter the task to be added : ")+'\n'
	elif len(sys.argv) == 2 and action=='done':
		text=raw_input("Please enter the s.no. of the completed task : ")+'\n'
	if len(sys.argv) > 2:
		text=sys.argv[2]+'\n'
		
	#~ Read the contents of the current file and store it in the dict
	task_dict=read()

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
			display()
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
	display()
	
def display():
	print '\n'+20*'*'+'\nTO-DO LIST\n'+20*'*'
	f=open("todo.txt")
	tasks=f.readlines()
	f.close()
	for t in tasks:
		print t,
	
def check(st):
	lol=[]
	try:
		m=re.search(r'(.+) #(.+)',st)
		lol.append(m.group(1))
		lol.append(m.group(2))
	except AttributeError:
		lol.append(st)
	return lol

if __name__=='__main__':
	main()

