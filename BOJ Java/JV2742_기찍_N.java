package JVtest2742;

import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter (System.out));
		BufferedReader A = new BufferedReader(new InputStreamReader (System.in));
		
		int num = Integer.parseInt(A.readLine());
		
		for(int i = num; i > 0; i--)
		{
			bw.write(i + "\n");
		}
		bw.flush();
		bw.close();
	}

}