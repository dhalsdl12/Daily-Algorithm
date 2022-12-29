package JVtest1552;

import java.io.*;
public class main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter (System.out));
		BufferedReader A = new BufferedReader(new InputStreamReader (System.in));
		
		int n = Integer.parseInt(A.readLine());
		
		for(int j = 0; j < n; j++)
		{
			String a = (A.readLine());
			String[] aa = a.split("\\s+");
			int[] bb = new int[2];
			for(int i = 0; i <aa.length; i++)
			{
				bb[i] = Integer.parseInt(aa[i]);
			}
			bw.write(bb[0]+bb[1] + "\n");
		}
		bw.flush();
		bw.close();
	}

}
