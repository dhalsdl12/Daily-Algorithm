package JVtest1065;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int cnt = 0;
	
		for(int i = 1; i <= num; i++)
		{
			if(i < 100)
				cnt++;
			else if(((i/100) - ((i%100)/10)) == (((i%100)/10) - (i%10)))
				cnt++;
		}
		System.out.println(cnt);
		sc.close();
	}
}
