package JVtest4948;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = 1;
		while(true)
		{
			num = sc.nextInt();
			int n = num*2;
			int cnt = 0;
			boolean data[] = new boolean[n+1];
			if(num == 0) break;
			
			data[0] = false;
			data[1] = false;
			for(int i = 2; i <= n; i++)
				data[i] = true;
			for(int i = 2; i <=n; i++)
			{
				for(int j = 2; i*j <= n; j++)
				{
					data[i*j] = false;
				}
			}
			for(int i = num+1; i <= n; i++)
			{
				if(data[i])
					cnt++;
			}
			
			System.out.println(cnt);
		}
		sc.close();
	}
}
