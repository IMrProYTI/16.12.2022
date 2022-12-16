/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <cstdlib>

using namespace std;

long a = 10;

long F(long n)
{
    if (n == 0)
    {
        return 0;
    }
    else
    {
        return F(div(n, a).quot) + div(n, a).rem;
    }
}

int main()
{
    long counter = 0;
    for (long i = 237567892; i <= 1134567009+1; i++)
    {
        if (F(i) > F(i + 1))
        {
            counter = counter + 1;
        }
    }
    
    cout << counter << endl;
    return 0;
}