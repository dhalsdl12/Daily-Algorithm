using System;
using static System.Console;

namespace CStest2750
{
    class CStest2750
    {
        static void Main(string[] args)
        {
            int num = int.Parse(ReadLine());
           
            int[] a = new int[num];
            int temp = 0;

            for(int i = 0; i < num; i++)
            {
                a[i] = int.Parse(ReadLine());
            }

            for(int i = 0; i < num; i++)
            {
                for(int j = 0; j < num-1; j++)
                {
                    if (a[j] > a[j + 1])
                    {
                        temp = a[j + 1];
                        a[j + 1] = a[j];
                        a[j] = temp;
                    }
                }
            }
            for (int i = 0; i < num; i++)
                WriteLine(a[i]);
        }
    }
}
