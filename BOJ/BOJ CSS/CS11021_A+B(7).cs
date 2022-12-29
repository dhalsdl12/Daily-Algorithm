using System;
using static System.Console;
using System.Text;

namespace CStest11021
{
    class CStest11021
    {
        static void Main(string[] args)
        {
            int max = int.Parse(ReadLine());
            int a, b;

            StringBuilder ab = new StringBuilder();

            for(int i = 0; i < max; i++)
            {
                string[] ss = ReadLine().Split();
                a = int.Parse(ss[0]);
                b = int.Parse(ss[1]);

                ab.Append("Case #" + (i+1) + ": " + (a + b) + "\n");
            }
            WriteLine(ab);
        }
    }
}
