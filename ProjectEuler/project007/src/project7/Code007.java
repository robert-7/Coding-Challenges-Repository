package project7;
import java.util.Arrays;

public class Code007 {
	public static void main(String[] args) {
		int n = Integer.parseInt(args[0]);
		int count = 1;
		int[] primes = new int[n]; primes[0]=2;
		int next_number = 3;
		
		while (count != n){
			for (int i = 0;i!=count;i++) {
				int prime = primes[i];
				if (next_number % prime == 0) {
					next_number++;
					break;
				} if (i == count-1) {
					primes[count] = next_number;
					count++;
					next_number++;
					break;
				}
			}
		}
		System.out.println(Arrays.toString(primes));
		
			
	}
}
