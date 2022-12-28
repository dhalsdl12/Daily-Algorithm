using System;
using static System.Console;
using System.Text;

namespace CStest1929
{
    class CStest1929
    {
        static void Main(string[] args)
        {
            string[] ss = ReadLine().Split();
            int min = int.Parse(ss[0]);
            int max = int.Parse(ss[1]);
            int cnt = 0;

            StringBuilder ab = new StringBuilder();

            for(int i = min; i <= max; i++)
            {
                cnt = 0;
                for(int j = 1; j <= i/2; j++)
                {
                    if (i % j == 0)
                        cnt++;
                }
                if (cnt == 1)
                    ab.Append(i + "\n");
            }
            WriteLine(ab);
        }
    }
}
