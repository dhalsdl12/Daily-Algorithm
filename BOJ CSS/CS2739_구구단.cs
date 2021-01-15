using System;
using static System.Console;

namespace CStest2739
{
    class CStest2739
    {
        static void Main(string[] args)
        {
            string num = ReadLine();
            int dan = int.Parse(num);

            for(int i = 0; i<9; i++)
            {
                WriteLine($"{dan} * {i+1} = {dan*(i+1)}");
            }
        }
    }
}
