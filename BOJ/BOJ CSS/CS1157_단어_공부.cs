using System;
using static System.Console;

namespace CStest1157
{
    class CStset1157
    {
        static void Main(string[] args)
        {
            string word = ReadLine();
            string upperword = word.ToUpper();

            int[] ascii = new int[26];

            for (int i = 0; i < 26; i++)
            {
                ascii[i] = 65 + i;
            }

            char[] spelling = upperword.ToCharArray();
            int[] cnt = new int[26];

            for(int i = 0; i < 26; i++)
            {
                cnt[i] = 0;

                for(int j = 0; j < spelling.Length; j++)
                {
                    if (ascii[i] == Convert.ToInt32(spelling[j]))
                        cnt[i]++;
                }
            }

            int maxcnt = 0;
            int maxvalue = 0;

            for (int i = 0; i < 26; i++)
            {
                if (maxcnt < cnt[i])
                {
                    maxcnt = cnt[i];
                    maxvalue = i;
                }
            }
            int count = 0;
            for(int i = 0; i < 26; i++)
            {
                if (cnt[maxvalue] == cnt[i])
                    count++;
            }
            if (count > 1)
                WriteLine("?");
            else
                WriteLine(Convert.ToChar(ascii[maxvalue]));

            
        }
    }
}