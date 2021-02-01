package JVtest5613;

import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int result = a;
		
		while(true)
		{
			String temp = sc.next();
			if(temp.equals("="))
				break;
			int b = sc.nextInt();
			
			if(temp.equals("+"))
				result += b;
			if(temp.equals("-"))
				result -= b;
			if(temp.equals("/"))
				result /= b;
			if(temp.equals("*"))
				result *= b;
		}
		System.out.println(result);
		sc.close();
	}

}