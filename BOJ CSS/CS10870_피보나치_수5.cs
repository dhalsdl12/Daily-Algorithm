using System;
using static System.Console;


namespace CStest10870
{
    class CStest10872
    {
        static void Main(string[] args)
        {
            int n = int.Parse(ReadLine());

            int[] fibo = new int[n];


            WriteLine(Fibo(n));
        }
        static int Fibo(int n)
        {
            if (n == 0)
                return 0;
            else if (n == 1)
                return 1;
            return Fibo(n - 1) + Fibo(n - 2);
        }


       /* static void Main(string[] args)
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
        }*/
    }
}
