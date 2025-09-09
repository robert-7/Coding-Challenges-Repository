package project8;

import java.util.ArrayList;
import java.util.Arrays;

public class Code008 {
	public static void main(String[] args) {
		String input =  "73167176531330624919225119674426574742355349194934" +
						"96983520312774506326239578318016984801869478851843" +
						"85861560789112949495459501737958331952853208805511" +
						"12540698747158523863050715693290963295227443043557" +
						"66896648950445244523161731856403098711121722383113" +
						"62229893423380308135336276614282806444486645238749" +
						"30358907296290491560440772390713810515859307960866" +
						"70172427121883998797908792274921901699720888093776" +
						"65727333001053367881220235421809751254540594752243" +
						"52584907711670556013604839586446706324415722155397" +
						"53697817977846174064955149290862569321978468622482" +
						"83972241375657056057490261407972968652414535100474" +
						"82166370484403199890008895243450658541227588666881" +
						"16427171479924442928230863465674813919123162824586" +
						"17866458359124566529476545682848912883142607690042" +
						"24219022671055626321111109370544217506941658960408" +
						"07198403850962455444362981230987879927244284909188" +
						"84580156166097919133875499200524063689912560717606" +
						"05886116467109405077541002256983155200055935729725" +
						"71636269561882670428252483600823257530420752963450";
		String[] input_split = input.split("0|1|2|3");
		ArrayList<String> input_split_fixed = new ArrayList<String>();
		for (int i=0;i!=input_split.length;i++) {
			int str_len = input_split[i].length();
			if (str_len == 5) {
				input_split_fixed.add(input_split[i]);
			} else if (str_len > 5) {
				for (int j=0;j!=str_len-4;j++) {
					input_split_fixed.add(input_split[i].substring(j, j+5));
				}
			}
		}
		
		int max = 0;
		for (int i=0;i!=input_split_fixed.size();i++) {
			String five_digit_number = input_split_fixed.get(i);
			int j0 = Integer.parseInt(
					String.valueOf(five_digit_number.charAt(0)));
			int j1 = Integer.parseInt(
					String.valueOf(five_digit_number.charAt(1)));
			int j2 = Integer.parseInt(
					String.valueOf(five_digit_number.charAt(2)));
			int j3 = Integer.parseInt(
					String.valueOf(five_digit_number.charAt(3)));
			int j4 = Integer.parseInt(
					String.valueOf(five_digit_number.charAt(4)));
			int product = j0*j1*j2*j3*j4;
			if (product > max) {
				max = product;
			}
		}
		System.out.println(input_split_fixed);
		System.out.println(max);
	}
}
