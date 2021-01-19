package JVtest1110;

import java.io.*;
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter (System.out));
		BufferedReader A = new BufferedReader(new InputStreamReader (System.in));
		
		int num = Integer.parseInt(A.readLine());
		int temp = num;
		int cnt = 0;
		
		while(true)
		{
			num = (num%10)*10 + (num/10+num%10)%10;
			cnt++;
			if(temp == num)
				break;
		}
		bw.write(cnt + "\n");
		bw.flush();
		bw.close();
	}

}
