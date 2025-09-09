package project6;

public class Code006 {

	public static void main(String[] args) {
		int n = Integer.parseInt(args[0]);
		int square_of_sum = (int) (Math.pow(n, 2) * Math.pow(n+1, 2) / 4);
		int sum_of_squares = (n)*(n+1)*(2*n+1) / 6;
		System.out.println(square_of_sum - sum_of_squares);
	}
	
}