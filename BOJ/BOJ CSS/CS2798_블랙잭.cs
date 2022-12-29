using System;
using static System.Console;
using System.Text;

namespace CStest2798
{
    class CStest2798
    {
        static void Main(string[] args)
        {
            string[] ss = ReadLine().Split();

            int n = int.Parse(ss[0]);
            int m = int.Parse(ss[1]);

            int result = 0;
            int max = 0;
            int[] array = new int[n];

            string[] card = ReadLine().Split();
            for(int i = 0; i < n; i++)
            {
                array[i] = int.Parse(card[i]);
            }

            for(int i = 0; i < n; i++)
            {
                for(int j = i+1; j < n; j++)
                {
                    for(int k = j+1; k < n; k++)
                    {
                        result = array[i] + array[j] + array[k];
                        if (result > max && result <= m)
                            max = result;
                    }
                }
            }
            WriteLine(max);
        }
    }
}
