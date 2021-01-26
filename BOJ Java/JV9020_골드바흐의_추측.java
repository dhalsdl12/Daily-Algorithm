package JVtest9020;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int n1 = 0, n2 = 0;
		int number = 0;
		for(int i = 0; i < num; i++)
		{
			number = sc.nextInt();
			for(n1 = number/2, n2 = number/2; ;n1--,n2++)
			{
				if(check(n1)&&check(n2))
				{
					System.out.println(n1 + " " + n2);
					break;
				}
			}
		}
		sc.close();
	}
	public static boolean check(int n)
	{
		for(int i = 2; i < n; i++)
		{
			if(n%i == 0)
				return false;
		}
		return true;
	}
}
