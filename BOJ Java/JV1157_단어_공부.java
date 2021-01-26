package JVtest1157;

import java.io.*;
public class Main {

	public static void main(String[] args) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter (System.out));
		BufferedReader A = new BufferedReader(new InputStreamReader (System.in));
		
		String word = (A.readLine()).toUpperCase();
		
		int cnt[] = new int[26];
		int count = 0;
		for(int i = 0; i < 26; i++)
		{
			cnt[i] = 0;
		}
		for(int i = 0; i < word.length(); i++)
		{
			for(int j = 0; j < 26; j++)
			{
				if(word.charAt(i) == (char)(65+j))
					cnt[j]++;
			}
		}
		int max = 0, max_val = 0;
		char max_word = 0;
		for(int i = 0; i < 26; i++)
		{
			if(max < cnt[i])
			{
				max = cnt[i];
				max_val = i;
				max_word = (char)(i+65);
			}
		}
		for(int i = 0; i < 26; i++)
		{
			if(cnt[max_val] == cnt[i])
				count++;
		}
		if(count > 1)
			System.out.println("?");
		else
			System.out.println(max_word);
		bw.flush();
		bw.close();
	}
}
