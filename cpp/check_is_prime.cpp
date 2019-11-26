#include <iostream>
using namespace std;
int main()
{
  int n, i, toContinue;
  bool isPrime;
  do
  {
    isPrime = true;
    cout << "Enter a positive integer: ";
    cin >> n;
    for(i = 2; i <= n / 2; ++i)
    {
        if(n % i == 0)
        {
            isPrime = false;
            break;
        }
    }
    if (isPrime)
        cout << n << " is a prime number" << endl;
    else
        cout << n << " is not a prime number" << endl;

    cout << "Continue? Enter 1 to continue, 0 to quit: ";
    cin >> toContinue;

  } while (toContinue != 0);

  return 0;
}
