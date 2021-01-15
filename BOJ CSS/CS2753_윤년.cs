using System;
using static System.Console;

namespace CStest2753
{
    class CStest2753
    {
        static void Main(string[] args)
        {
            string year = ReadLine();
            int a = int.Parse(year);

            if (a % 4 == 0 && a % 100 != 0)
                WriteLine("1");
            else if (a % 400 == 0)
                WriteLine("1");
            else
                WriteLine("0");
        }
    }
}
