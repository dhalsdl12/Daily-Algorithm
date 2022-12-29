package JVtest10809;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String a = sc.nextLine();
		int num[] = new int[26];
		
		for(int i = 0; i < num.length; i++)
		{
			num[i] = -1;
		}
		
		for(int i = 0; i < a.length(); i++)
		{
			char c = a.charAt(i);
			
			if(num[c-'a'] == -1)
				num[c-'a'] = i;
		}
		for(int i = 0; i < num.length; i++)
		{
			System.out.print(num[i] + " ");
		}
		sc.close();
	}
}