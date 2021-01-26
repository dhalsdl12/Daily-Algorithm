package JVtest2292;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int number = 1, upcnt = 6, count = 1;
		while(num > number)
		{
			number += upcnt;
			upcnt += 6;
			count++;
		}
		System.out.println(count);
		sc.close();
	}
}
