using System;
using static System.Console;

namespace CStest1546
{
    class CStest1546
    {
        static void Main(string[] args)
        {
            int num = int.Parse(ReadLine());
  
            string[] ss = ReadLine().Split();
            float[] score = Array.ConvertAll(ss, float.Parse);

            float maxscore = float.MinValue;

            for(int i = 0; i < num; i++)
            {
                if (maxscore < score[i])
                    maxscore = score[i];
            }
            float sum = 0;
            for (int i = 0; i < num; i++)
            {
                score[i] = (score[i] / maxscore) * 100;
                sum = sum + score[i];
            }
            double Avg = sum / num;

            WriteLine(Avg);
        }
    }
}
