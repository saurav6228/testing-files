from random import *
import os

def main():
	start = 2
	end = 10
	for tnum in range(start,end):
		script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
		testnum = str(tnum)
		if(tnum<10):
			rel_path = "input/input0"+testnum+".txt"
		else:
			rel_path = "input/input"+testnum+".txt"
		
		abs_file_path = os.path.join(script_dir, rel_path)
		file = open(abs_file_path,"w")
		T = 30;
		#T = randint(1,100)
		#K = randint(0,100)
		file.write("%d\n"%(T))
		for i in range(10):
			rnd1 = randint(1,100000)
			rnn = randint(1,100)
			#rnd2 = randint(1,pow(2,31)-1)
			rnd2 = rnd1*rnn
			file.write("%d %d\n"%(rnd1,rnd2))
		for i in range(10,20):
			rnd1 = randint(1,10000)
			#rnn = randint(1,100)
			rnd2 = randint(100000,100000000)
			#rnd2 = rnd1*rnn
			file.write("%d %d\n"%(rnd1,rnd2))		
		for i in range(20,30):
			rnd1 = randint(1000,1000000)
			#rnn = randint(1,100)
			rnd2 = randint(1000000,100000000)

			#rnd2 = rnd1*rnn
			file.write("%d %d\n"%(rnd1,rnd2))	
		file.close()














if __name__ =="__main__":
	main()