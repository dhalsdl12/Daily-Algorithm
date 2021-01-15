using System;
using static System.Console;


namespace CStest10872
{
    class CStest10872
    {
        static void Main(string[] args)
        {
            int n = int.Parse(ReadLine());
            int Factorial = 0;
            WriteLine(Fac(n));
        }
        static int Fac(int n)
        {
            if (n == 0 || n == 1)
                return 1;
            
            return n * Fac(n - 1);
        }
    }
}
