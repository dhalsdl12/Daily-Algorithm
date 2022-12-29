package JVtest1978;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int number[] = new int[num];
		int count = 0, cnt = 0;
		for(int i = 0; i < num; i++)
		{
			number[i] = sc.nextInt();
			if(number[i] == 1)
				continue;
			cnt = 0;
			for(int l = 1; l < number[i]; l++)
			{
				if(number[i]%l == 0)
				{
					cnt++;
				}
			}
			if(cnt == 1)
				count++;
		}
		System.out.println(count);
		sc.close();
	}
}
