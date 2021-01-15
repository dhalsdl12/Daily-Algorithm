using System;
using static System.Console;

namespace CStest2908
{
    class CStest2908
    {
        static void Main(string[] args)
        {
            string[] num = ReadLine().Split();

            int num1 = int.Parse(num[0]);
            int num2 = int.Parse(num[1]);

            int temp1 = (num1 / 100) + ((num1 % 100) / 10) * 10 + (num1 % 10) * 100;
            int temp2 = (num2 / 100) + ((num2 % 100) / 10) * 10 + (num2 % 10) * 100;

            if (temp1 > temp2)
                WriteLine(temp1);
            else
                WriteLine(temp2);
        }
    }
}
