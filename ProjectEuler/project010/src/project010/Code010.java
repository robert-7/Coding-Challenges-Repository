package project010;

import java.util.ArrayList;
import java.util.Arrays;

public class Code010 {
	public static ArrayList<Integer> main(String[] args) {
		int n = Integer.parseInt(args[0]);
		int count = 1; long sum = 0;
		ArrayList<Integer> primes = new ArrayList<Integer>(); primes.add(2);
		int next_number = 3;
		
		while (next_number != n){
			for (int i = 0;i!=count;i++) {
				int prime = primes.get(i);
				if (next_number % prime == 0) {
					next_number++;
					break;
				} if (i == count-1) {
					primes.add(next_number);
					sum += next_number;
					count++;
					next_number++;
					break;
				}
			}
		}
		//System.out.println(primes);
		//System.out.println(sum);
		return primes;	
	}
}
