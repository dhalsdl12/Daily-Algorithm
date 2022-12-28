using System;
using static System.Console;

namespace CStest8393
{
    class CStest8393
    {
        static void Main(string[] args)
        {
            string num = ReadLine();
            int num1 = int.Parse(num);
            int sum = 0;

            for (int i = 1; i <= num1;i++)
            {
                sum = sum + i;
            }
            WriteLine(sum);
        }
    }
}
