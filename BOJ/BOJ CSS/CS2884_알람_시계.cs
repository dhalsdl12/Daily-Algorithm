using System;
using static System.Console;

namespace CStest2884
{
    class CStest2884
    {
        static void Main(string[] args)
        {
            string s = ReadLine();
            string[] ss = s.Split();

            int H = int.Parse(ss[0]);
            int M = int.Parse(ss[1]);

            int aH;
            int aM;

            aM = M - 45;
            if (aM >= 0)
            {
                aH = H;
                WriteLine($"{aH} {aM}");
            }
            else
            {
                aM = aM + 60;
                aH = H - 1;
                if (aH < 0)
                    aH = aH + 24;
                WriteLine($"{aH} {aM}");
            }
        }
    }
}
