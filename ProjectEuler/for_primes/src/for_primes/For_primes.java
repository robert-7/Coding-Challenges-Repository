package for_primes;

import java.util.ArrayList;

import project010.Code010;

public class For_primes {
	public static void main(String[] args) {
		String[] arg = {"1000"};
		ArrayList<Integer> primes = Code010.main(arg);
		System.out.println("y\tx\tb\ta");
		for (int i = 0; i!=primes.size()-1; i++) {
			int curr_prime = primes.get(i);
			int next_prime = primes.get(i+1);
			int curr_mult = 1;
			int next_mult = 1;
			int curr_value = curr_prime*curr_mult;
			int next_value = next_prime*next_mult;
			while(true) {
				while (curr_value<next_value) {
					if (next_value-curr_value==1) {
						System.out.println(
								Integer.toString(primes.get(i+1))+
								"\t"+Integer.toString(primes.get(i))+
								"\t"+Integer.toString(next_mult)+
								"\t"+Integer.toString((-1)*curr_mult));
						break;
					} else {
						curr_mult++; 
						curr_value = curr_prime*curr_mult;
					}
				} 
				if (next_value-curr_value!=1) {
					next_mult++; 
					next_value = next_prime*next_mult;
				} else {
					break;
				}
			}
		}
	}
}
