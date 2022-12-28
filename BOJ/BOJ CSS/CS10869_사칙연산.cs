using System;
using static System.Console;

namespace CStest10869
{
    class CStest10869
    {
        static void Main(string[] args)
        {
            string[] ss = ReadLine().Split();

            int a = int.Parse(ss[0]);
            int b = int.Parse(ss[1]);

            WriteLine(a + b);
            WriteLine(a - b);
            WriteLine(a * b);
            WriteLine(a / b);
            WriteLine(a % b);
        }
    }
}
