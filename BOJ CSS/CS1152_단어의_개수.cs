using System;
using static System.Console;

namespace CStest1152
{
    class CStest1152
    {
        static void Main(string[] args)
        {
            string word = ReadLine().Trim();

            char[] words = word.ToCharArray();

            int cnt = 0;
            
            for(int i = 0; i < words.Length; i++)
            {
                if (words[i] == ' ')
                {
                    if (words[i - 1] == ' ')
                        continue;
                    else
                        cnt++;
                }
            }
            WriteLine(cnt + 1);
        }
    }
}
