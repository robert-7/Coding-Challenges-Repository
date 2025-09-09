package project13;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class Code013 {
	public static void main(String[] args) throws IOException {
		
		// Read the file
		String file = args[0];
		BufferedReader br = new BufferedReader(new FileReader(file));
		String line; int i = 0;
		ArrayList<int[]> numbersAsStrings = new ArrayList<int[]>();
		int numberOfLines;
		int numberOfDigits = 50; 
		int numberOfDigitsWithExtra = numberOfDigits+1; 
		// for every line in the numbers file
		while ((line = br.readLine()) != null) {
			// we want to add the indices to the int array
			numbersAsStrings.add(new int[numberOfDigitsWithExtra]);
			for (int j = 0; j != numberOfDigits; j++) {
				numbersAsStrings.get(i)[j+1] = Integer.parseInt(line.charAt(j)+"");
			} numbersAsStrings.get(i)[0] = 0; // set the extra digit to zero
			i++;
		} numberOfLines = i;
		br.close();
		
		// let's add two more arrays to numbersAsStrings
		// the first will hold on to the sum of the digits in that index / 10
		// i.e. the number we insert
		// the second will hold on to the sum of the digits in that index % 10
		// i.e. the carry-over number
		numbersAsStrings.add(new int[numberOfDigitsWithExtra]);
		numbersAsStrings.add(new int[numberOfDigitsWithExtra]);
		numbersAsStrings.add(new int[numberOfDigitsWithExtra]);
		
		int indexOfSum = numberOfLines;
		int indexOfCarry = indexOfSum+1;
		int indexOfDigitRecorded = indexOfCarry+1;
		
		// note that the last index will be a zero...
		// since we haven't carried over any numbers yet
		numbersAsStrings.get(numbersAsStrings.size()-1)[0] = 0;
		
		int sum;
		int remainder = 0;
		for (int j=numberOfDigits; j!=-1; j--) {
			sum = 0;
			for (i=0; i!=numbersAsStrings.size()-1; i++) {
				sum += numbersAsStrings.get(i)[j];
			} 
			numbersAsStrings.get(indexOfSum)[j] = sum;
			numbersAsStrings.get(indexOfDigitRecorded)[j] = sum % 10;
			if (j!=0) {
				numbersAsStrings.get(indexOfCarry)[j-1] = sum / 10;
			} else {
				remainder = sum / 10;
			}
		}
		
		for (i=0; i!=indexOfDigitRecorded+1; i++) {
			System.out.println(i + " " + Arrays.toString(numbersAsStrings.get(i)));
		}
		
		int k=5;
		int L=k+2;
		
// 		to add all the numbers together, we need to add each index
//		long sum = 0; long sum2 = 0; long sum3 = 0;
//		while ((line = br.readLine()) != null) {
//			sum += Long.parseLong(line.substring(0, 15), 10);
//			sum2 += Long.parseLong(line.substring(0, 16), 10);
//			sum3 += Long.parseLong(line.substring(0, 18), 10);
//		}
//		br.close();
//		System.out.println(sum);
//		System.out.println(sum2);
//		System.out.println(sum3);
	}
}
