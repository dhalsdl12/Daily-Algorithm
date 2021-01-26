package JVtest2941;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String word = sc.nextLine();
		sc.close();
		String[] cro = {"c=","c-","dz=","d-","lj","nj","s=","z="};
		for(int i = 0; i < cro.length; i++)
		{
			word = word.replace(cro[i], "a");
		}
		System.out.println(word.length());
	}
}
