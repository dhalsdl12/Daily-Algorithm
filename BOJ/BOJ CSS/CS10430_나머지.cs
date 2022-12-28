using System;
using static System.Console;

namespace CStest10430
{
    class CStest10430
    {
        static void Main(string[] args)
        {
            string[] ss = ReadLine().Split();

            int a = int.Parse(ss[0]);
            int b = int.Parse(ss[1]);
            int c = int.Parse(ss[2]);

            WriteLine((a + b) % c);
            WriteLine(((a % c) + (b % c)) % c);
            WriteLine((a * b) % c);
            WriteLine(((a % c) * (b % c)) % c);
        }
    }
}
