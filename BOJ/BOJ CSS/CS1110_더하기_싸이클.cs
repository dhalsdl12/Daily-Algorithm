using System;
using static System.Console;

namespace CStest1110
{
    class CStest1110
    {
        static void Main(string[] args)
        {
            string num = ReadLine();
            int cnt = 0;
            int add;
            if (int.Parse(num) <= 9)
                num = num + 0;

            string origin = num;
            while(true)
            {
                cnt++;
                int a = int.Parse(num) / 10;
                int b = int.Parse(num) % 10;

                add = a + b;

                num = b.ToString() + (add % 10).ToString();

                if (int.Parse(origin) == int.Parse(num))
                    break;
            }
            WriteLine(cnt);
        }
    }
}
