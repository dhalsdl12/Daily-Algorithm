using System;
using System.Text;
using static System.Console;

namespace CStest1065
{
    class CStest1065
    {
        static void Main(string[] args)
        {
            int cnt = 0;

            int num = int.Parse(ReadLine());

            for(int i = 1; i <= num; i++)
            {
                if (Hansu(i.ToString()))
                    cnt++;
            }
            WriteLine(cnt);
        }
        static bool Hansu(string i)
        {
            if (int.Parse(i) < 100)
                return true;

            int[] num = new int[i.Length];
            for(int a = 0; a < i.Length; a++)
            {
                num[a] = int.Parse(i[a].ToString());
            }

            if (num[0] - num[1] == num[1] - num[2])
                return true;
            else
                return false;
        }
    }
}
