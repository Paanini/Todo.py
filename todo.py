import re, sys, sqlite3
def main():
	#~ Declare the important variables
	try:
		action=sys.argv[1]
	except IndexError:
		action=raw_input("Pleae enter an option - \n- add\n- done\n- list\n Enter your option: ")
	
	#Connect to an SQLite DB and create the cursor
	conn=sqlite3.connect("todo.db")
	c=conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS tasks (s_no integer unique, task text, tag text, pri text check(pri in ('High','Low','Medium','None')));")
	index=c.execute("select count(*) from tasks").fetchall()[0][0]+1

	if len(sys.argv) > 2:
		text=sys.argv[2]
	else:
		if action=='add':
			text=raw_input("Please enter the task to be added : ")+'\n'
		elif action=='done':
			text=raw_input("Please enter the s.no. of the completed task : ")+'\n'
	
	record=[(index,text,"tag","High")]
	#~ print record
	if action=='add':
		yoyo=add(c,record)
		print yoyo,"\n One task added"
	elif action=='done':
		done(c,record)
	conn.commit()

def add(c,record):
	#~ print record
	c.executemany("INSERT INTO tasks VALUES(?,?,?,?)",record)
	#~ c.commit()
	a=c.execute("select * from tasks")
	return a.fetchall()
	
def remove(c,record):
	c.execute("DELETE FROM tasks WHERE s_no=?",record[0][1])
		

if __name__=='__main__':
	main()
