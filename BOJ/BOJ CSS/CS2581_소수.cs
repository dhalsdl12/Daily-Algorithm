using System;
using static System.Console;
namespace CStest2581
{
    class CStest2581
    {
        static void Main(string[] args)
        {
            int a = int.Parse(ReadLine());
            int b = int.Parse(ReadLine());
            int min = b;
            int cnt = 0;
            int sum = 0;

            for(int i = b; i >= a; i--)
            {
                cnt = 0;
                for(int j = i-1; j >= 1; j--)
                {
                    if (i % j == 0)
                        cnt++;
                }
                if (cnt == 1)
                {
                    sum = sum + i;
                    if (i < min)
                        min = i;
                }
            }
            if (sum == 0)
                WriteLine("-1");
            else
            {
                WriteLine(sum);
                WriteLine(min);
            }
            
        }
    }
}
