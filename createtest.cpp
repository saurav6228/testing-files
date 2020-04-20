// C program for generating a
// random number in a given range.
#include<bits/stdc++.h>
#include<string>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define int long long
// Generates and prints 'count' random
// numbers in range [lower, upper].
using namespace std;
void printrand(int lower, int upper)
{
		int num = (rand() % (upper - lower + 1)) + lower;
		printf("%d ", num);

}

// Driver code
int main()
{
      int num = 0;
      srand(time(0));

      string s = "C:\\Users\\Saurav Singh\\Desktop\\testing\\input\\input"+ to_string(num) + ".txt";
      freopen (s, "w", stdout);


	printrand(1,100000);




	fclose(stdout);

	return 0;
}
