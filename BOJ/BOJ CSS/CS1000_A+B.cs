using System;

namespace CStest1000
{
    class CStest1000
    {
        static void Main(string[] args)
        {
            string s = Console.ReadLine();
            string[] ss = s.Split();

            int a = int.Parse(ss[0]);
            int b = int.Parse(ss[1]);

            Console.WriteLine(a + b);

        }
    }
}
