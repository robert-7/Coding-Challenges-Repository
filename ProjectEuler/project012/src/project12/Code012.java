package project12;

public class Code012 {
	public static void main(String[] args) {
		int need_num_factors = Integer.parseInt(args[0]);
		int i = 1; 
		int triangle = (i)*(i+1)/2;
		int num_factors = 0;
		do {
			i++;
			triangle = (i)*(i+1)/2;
			num_factors = factors(triangle);
		} while (num_factors < need_num_factors);
		System.out.println("Final: " + triangle);
		
	}

	private static int factors(int triangle) {
		// we know i and j are co-prime
		int count = 0;
		for (int factor=1;factor!=(triangle+2)/2;factor++) {
			if (triangle%factor==0){
				count++;
			}
		}
		System.out.println("Triangle: " + triangle + " Count: " + count);
		return count;
	}
}

/*while (found == false) {
if (i%2==0) { 	// i is even
	num_factors = factors(i/2,i+1);
} else { 		// i is odd
	num_factors = factors(i, (i+1)/2);
}

if (num_factors >= need_num_factors) {
	System.out.println((i)*(i+1)/2);
	break;
}

i++;
}*/


/*private static int factors(int i1, int i2) {
	// we know i and j are co-prime
	int count = 1;
	for (int factor=2;factor!=Math.max(i1,i2)+1;factor++) {
		if ((i1%factor==0)||(i2%factor==0)) {
			count++;
		}
	}
	return count;
}*/
