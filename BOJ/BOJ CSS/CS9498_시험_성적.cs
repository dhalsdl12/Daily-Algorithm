using System;
using static System.Console;

namespace CStest9498
{
    class CStest9498
    {
        static void Main(string[] args)
        {
            string score = ReadLine();
            int a = int.Parse(score);

            if (a >= 90)
                WriteLine("A");
            else if (a >= 80)
                WriteLine("B");
            else if (a >= 70)
                WriteLine("C");
            else if (a >= 60)
                WriteLine("D");
            else
                WriteLine("F");
        }
    }
}
