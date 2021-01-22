package JVtest2609;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n1 = sc.nextInt(),n2 = sc.nextInt();
		int g = 0, l;
		for(int i = 1; i <= n1; i++)
		{
			if(n1%i == 0 && n2%i == 0)
				g = i;
		}
		l = n1*n2/g;
		System.out.println(g);
		System.out.println(l);
		sc.close();
	}
}
