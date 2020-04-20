from random import *
import os

def main():
	start = 25
	end = 31
	for tnum in range(start,end):
		script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
		testnum = str(tnum)
		if(tnum<10):
			rel_path = "input/input0"+testnum+".txt"
		else:
			rel_path = "input/input"+testnum+".txt"
		
		abs_file_path = os.path.join(script_dir, rel_path)
		file = open(abs_file_path,"w")
		N = randint(1,100000)
		K = randint(0,1000000)
		file.write("%d %d\n"%(N,K))
		for i in range(N):
			rnd = randint(100000,1000000000000)
			file.write("%d "%(rnd))
		file.close()














if __name__ =="__main__":
	main()