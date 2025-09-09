package project9;

public class Code009 {
	public static void main(String[] args) {
		int b = 0; int rem;
		do {
			b++;
			rem = (500000-1000*b)%(1000-b);
		} while (rem != 0);
		System.out.println(b);
		int a = (500000-1000*b)/(1000-b);
		System.out.println(a);
		System.out.println(a*b*Math.pow(a*a+b*b,0.5));
	
	} 
}
