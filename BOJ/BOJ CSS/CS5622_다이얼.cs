using System;
using static System.Console;
using System.Text;

namespace CStest5622
{
    class CStest5622
    {
        static void Main(string[] args)
        {
            int[] dial = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 };

            int[] time = new int[dial.Length];
            int alltime = 0;

            for(int i = 0; i < dial.Length; i++)
            {
                time[i] = i + 2;
            }

            string al = ReadLine();
            char[] all = al.ToCharArray();

            for(int j = 0; j < al.Length; j++)
            {
                if (Convert.ToInt32(all[j]) <= 67)
                    alltime += time[1];
                else if (Convert.ToInt32(all[j]) <= 70)
                    alltime += time[2];
                else if (Convert.ToInt32(all[j]) <= 73)
                    alltime += time[3];
                else if (Convert.ToInt32(all[j]) <= 76)
                    alltime += time[4];
                else if (Convert.ToInt32(all[j]) <= 79)
                    alltime += time[5];
                else if (Convert.ToInt32(all[j]) <= 83)
                    alltime += time[6];
                else if (Convert.ToInt32(all[j]) <= 86)
                    alltime += time[7];
                else if (Convert.ToInt32(all[j]) <= 90)
                    alltime += time[8];
            }
            WriteLine(alltime);
        }
    }
}
