using System;
using static System.Console;
using System.Text;

namespace CStest11022
{
    class CStest11022
    {
        static void Main(string[] args)
        {
            int max = int.Parse(ReadLine());

            StringBuilder ab = new StringBuilder();

            int a, b;

            for(int i = 0; i < max; i++)
            {
                string[] ss = ReadLine().Split();
                a = int.Parse(ss[0]);
                b = int.Parse(ss[1]);

                ab.Append("Case #" + (i + 1) + ": " + a + " + " + b + " = " + (a + b) + "\n");
            }
            WriteLine(ab);
        }
    }
}
