package JVtest1316;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int count = 0;
		int bool = 1;
		for(int i = 0; i < num; i++)
		{
			String word = sc.next();
			for(int j = 0; j < word.length(); j++)
			{
				if(j != word.length()-1)
				{
					if(word.charAt(j) == word.charAt(j+1))
					{
						continue;
					}
					else
					{
						for(int k = j+1; k < word.length();k++)
						{	
							bool = 1;
							if(word.charAt(j) == word.charAt(k))
							{
								bool = 0;
								break;
							}
						}
						if(bool == 0)
							break;
					}
				}
				else
					count++;
			}
		}
		System.out.println(count);
		sc.close();
	}
}
