using System;
using static System.Console;

namespace CStest2839
{
    class Program
    {
        static void Main(string[] args)
        {
            int kg = int.Parse(ReadLine());

            int bag = 0;

            while(kg > 0)
            {
                if(kg%5 == 0)
                {
                    kg -= 5;
                    bag++;
                }
                else if(kg%3 == 0)
                {
                    kg -= 3;
                    bag++;
                }
                else if(kg > 5)
                {
                    kg -= 5;
                    bag++;
                }
                else
                {
                    bag = -1;
                    break;
                }
            }
            WriteLine(bag);
        }
    }
}
