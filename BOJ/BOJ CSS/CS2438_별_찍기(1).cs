using System;
using static System.Console;

namespace CStest2438
{
    class CStest2438
    {
        static void Main(string[] args)
        {
            int num = int.Parse(ReadLine());

            for(int i = 0; i < num; i++)
            {
                for(int j = 0; j <= i; j++)
                {
                    Write("*");
                }
                WriteLine();
            }
        }
    }
}
