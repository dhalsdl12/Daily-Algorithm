using System;
using static System.Console;

namespace CStest1978
{
    class CStest1978
    {
        static void Main(string[] args)
        {
            int num = int.Parse(ReadLine());

            string[] ss = ReadLine().Split();

            int count = 0;
            int cnt = 0;
            for(int i = 0; i < num; i++)
            {
                int a = int.Parse(ss[i]);
                cnt = 0;
                for (int j = 1; j < a; j++)
                {
                    if (a % j == 0)
                        cnt++;
                }
                if (cnt == 1)
                    count++;
            }
            WriteLine(count);
        }
    }
}
