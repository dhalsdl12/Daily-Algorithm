package JVtest1002;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int x1,x2,y1,y2,r1,r2;
		double dist = 0;
		for(int i = 0; i < num; i++)
		{
			x1 = sc.nextInt();
		    y1 = sc.nextInt();
		    r1 = sc.nextInt();

		    x2 = sc.nextInt();
		    y2 = sc.nextInt();
		    r2 = sc.nextInt();
		    
		    dist = Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
			int n = 0;
		    if (r1 + r2 < dist)
		    	n = 1;
		    if (r1 + r2 == dist)
		    	n = 2;
		    if (r1 + r2 > dist)
		        n = 3;
		    if (Math.abs(r1 - r2) == dist)
		        n = 4;
		    if (Math.abs(r1 - r2) > dist)
		        n = 5;
		    if (x1 == x2 && y1 == y2 && r1 == r2)
		        n = 6;

		    switch (n) {
		    case 1:
		        System.out.println(0);
		        break;
		    case 2:
		        System.out.println(1);
		        break;
		    case 3:
		        System.out.println(2);
		        break;
		    case 4:
		        System.out.println(1);
		        break;
		    case 5:
		        System.out.println(0);
		        break;
		    case 6:
		        System.out.println(-1);
		        break;
		    }
		}
		sc.close();
	}
}
