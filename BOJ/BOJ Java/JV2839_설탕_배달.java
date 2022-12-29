package JVtest2839;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int count = 0;
		while(num != 0)
		{
			if(num%5 == 0)
			{
				num -= 5;
				count++;
			}
			else if(num%3 == 0)
			{
				count++;
				num -= 3;
			}
			else if(num > 5)
			{
				num -= 5;
				count++;
			}
			else
			{
				count = -1;
				break;
			}
		}
		System.out.println(count);
		sc.close();
	}
}
