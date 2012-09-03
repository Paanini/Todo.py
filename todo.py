import sys
def main():
	#~ Declare the important variables
	action=sys.argv[1]
	if len(sys.argv) > 2:
		text=sys.argv[2]
	#~ Read the contents of the current file and store it in the dict
	task_dict=read()
	if action=='add':
		for i in xrange(1,len(task_dict)+2):
			#~ print i
			if not task_dict.has_key(i):
				task_dict[i]=text
				break
		write(task_dict)
	


#~ task_dict={1:'one',2:'two',4:'three'}
#~ task_dict.pop(2)


def read():
	try:
		todo=open("todo.txt")
		tasks=todo.readlines()
		todo.close()
		#~ print "I have entered try"
		task_dict={}
		for t in tasks:
			task_dict[t[0]]=t[3:]
		#~ print task_dict
		return task_dict
	except IOError:
		todo=open("todo.txt","w")
		print "File does not exist. New file has been created"
		todo.close()
		return {}

def write (task_dict):
	f=open("todo.txt","w")
	for a,b in task_dict.iteritems():
		f.write(str(a)+'. '+b)
	f.close()
	display()
	
def display():
	f=open("todo.txt")
	tasks=f.readlines()
	for t in tasks:
		print t,
	
if __name__=='__main__':
	main()
