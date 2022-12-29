using System;
using static System.Console;

namespace CStest10950
{
    class CStest10950
    {
        static void Main(string[] args)
        {
            string s = ReadLine();
            int num = int.Parse(s);

            for(int i = 0; i < num; i++)
            {
                string ss = ReadLine();
                string[] sss = ss.Split();
                int a = int.Parse(sss[0]);
                int b = int.Parse(sss[1]);

                WriteLine(a+b);
            }
        }
    }
}
