using System;
using static System.Console;

namespace CStest1330
{
    class CStest1330
    {
        static void Main(string[] args)
        {
            string s = ReadLine();
            string[] ss = s.Split();

            int a = int.Parse(ss[0]);
            int b = int.Parse(ss[1]);

            if (a > b)
                WriteLine(">");
            else if (a < b)
                WriteLine("<");
            else
                WriteLine("==");
        }
    }
}
