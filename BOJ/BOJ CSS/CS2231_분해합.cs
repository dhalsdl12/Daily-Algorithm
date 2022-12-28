using System;
using static System.Console;
namespace CStest2231
{
    class CStest2231
    {
        static void Main(string[] args)
        {
            int num = int.Parse(ReadLine());
            int n = 0;
            int number = 0;

            for(int i = 1; i < num; i++)
            {
                if (i < 10)
                    n = i + i;
                else if (i < 100)
                    n = i + i / 10 + i % 10;
                else if (i < 1000)
                    n = i + i / 100 + (i % 100) / 10 + i % 10;
                else if (i < 10000)
                    n = i + i / 1000 + (i % 1000) / 100 + (i % 100) / 10 + i % 10;
                else if (i < 100000)
                    n = i + i / 10000 + (i % 10000) / 1000 + (i % 1000) / 100 + (i % 100) / 10 + i % 10;
                else if (i < 1000000)
                    n = i + i / 100000 + (i % 100000) / 10000 + (i % 10000) / 1000 + (i % 1000) / 100 + (i % 100) / 10 + i % 10;

                if (n == num)
                {
                    number = i;
                    break;
                }
            }
            if (number == 0)
                WriteLine("0");
            else
                WriteLine(number);
        }
    }
}
