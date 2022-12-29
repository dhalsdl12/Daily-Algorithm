using System;
using static System.Console;
using System.Text;


namespace CStest4344
{
    class CStest4344
    {
        static void Main(string[] args)
        {
            int num = int.Parse(ReadLine());
            double sum = 0;
            double cnt = 0;

            for(int i = 0; i < num; i++)
            {
                string[] ss = ReadLine().Split();
                double a = double.Parse(ss[0]);

                for(int j = 1; j < ss.Length; j++)
                {
                    sum += double.Parse(ss[j]);
                }
                sum = sum / a;
                for(int k = 1; k <= a; k++)
                {
                    if (double.Parse(ss[k]) > sum)
                        cnt += 1;
                }
                cnt = cnt *100 / a;
                WriteLine($"{cnt:F3}%");

                cnt = 0;
                sum = 0;
            }
        }
    }
}
