package JVtest4344;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		double per[] = new double[num];
		for(int i = 0; i < num; i++)
		{
			int n = sc.nextInt();
			int score[] = new int[n];
			double sum = 0, cnt = 0;
			for(int j = 0; j < n; j++)
			{
				score[j] = sc.nextInt();
				sum += score[j];
			}
			sum = sum/n;
			for(int k = 0; k < n; k++)
			{
				if(score[k] > sum)
					cnt++;
			}
			per[i] = cnt*100/n;
		}
		for(int i = 0; i < num; i++)
			System.out.println(String.format("%.3f", per[i]) + "%");
		
		sc.close();
	}
}
