using System;
using static System.Console;
using System.Text;


namespace CStest2741
{
    class CStest2741
    {
        static void Main(string[] args)
        {
            int max = int.Parse(ReadLine());

            StringBuilder ab = new StringBuilder();

            for (int i = 1; i <= max; i++)
            {
                ab.Append(i + "\n");
            }
            WriteLine(ab);
        }
    }
}
