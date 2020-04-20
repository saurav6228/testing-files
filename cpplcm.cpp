
#include <iostream>
#include <vector>
#include <fstream>
using namespace std;



int main()
{

    int start = 0;
    int end = 21;

    for(int tcase=start;tcase<end;tcase++)
    {
        string file1,file2;
        if(tcase<10){
             file1 = "./input/input0"+ to_string(tcase) + ".txt";
             file2 = "./output/output0"+ to_string(tcase) + ".txt";
        }
        else
        {
             file1 = "./input/input"+ to_string(tcase) + ".txt";
             file2 = "./output/output"+ to_string(tcase) + ".txt";
        }



            ifstream in;
            in.open(file1,ios::in);
            ofstream out;
            out.open(file2,ios::out);

                       int tc,a,b;
                   in>>tc;
                    while(tc--){
                       in>>a>>b;
                        if(b%a!=0)out<< "-1\n" ;
                        else out<<a<<" " <<b<<"\n";
                    }


           in.close();
           out.close();

    }

    return 0;
}
