using System;
using static System.Console;

namespace CStest14681
{
    class CStest14681
    {
        static void Main(string[] args)
        {
            string a = ReadLine();
            string b = ReadLine();

            int x = int.Parse(a);
            int y = int.Parse(b);

            if (x > 0 && y > 0)
                WriteLine("1");
            else if (x > 0 && y < 0)
                WriteLine("4");
            else if (x < 0 && y > 0)
                WriteLine("2");
            else if (x < 0 && y < 0)
                WriteLine("3");
        }
    }
}
