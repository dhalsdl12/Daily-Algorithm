using System;
using static System.Console;

namespace CStest2941
{
    class CStest2941
    {
        static void Main(string[] args)
        {
            string word = ReadLine();
            string[] Cro = { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};

            for(int i = 0; i < Cro.Length; i++)
            {
                word = word.Replace(Cro[i], "a");
            }
            WriteLine(word.Length);
        }
    }
}
