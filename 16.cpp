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
        return F(div(n, a).quot) + div(n, a).quot;
    }
}

int main()
{
    long counter = 0;
    for (long i = 237567892; i <= 1134567009; i++)
    {
        if (F(i) > F(i + 1))
        {
            counter = counter + 1;
        }
    }
    
    cout << counter << endl;
    return 0;
}