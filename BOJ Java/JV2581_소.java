package JV2581;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n1 = sc.nextInt();
		int n2 = sc.nextInt();
		int cnt = 0, sum = 0, min = n2;
		for(int i = n1; i <= n2; i++)
		{
			cnt = 0;
			if(i == 1)
				continue;
			for(int j = 1; j < i; j++)
			{
				if(i%j == 0)
					cnt++;
			}
			if(cnt == 1)
			{
				sum += i;
				if(i < min)
					min = i;
			}
		}
		if(sum == 0)
			System.out.println(-1);
		else
		{
			System.out.println(sum);
			System.out.println(min);
		}
		sc.close();
	}
}
