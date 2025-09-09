package project014;

import java.util.Hashtable;
import java.util.Map.Entry;

public class Code014 {
	
	public static Hashtable<Long, Long> dict = 
			new Hashtable<Long, Long>();
	
	public static void main(String[] args) {
		// we'll find solutions recursively
		// since recursions require an initial condition, we need to define 
		// one as having length one
		dict.put(1L, 1L);
		Long i;
		int MAX_INDEX = Integer.parseInt(args[0]);
		for(i=1L;i!=MAX_INDEX;i++) {
			handle(i);
			System.out.println(i+" has val "+dict.get(i));
		} 
		
		Long maxKey=null;
		Long maxValue = 0L; 
		for(Entry<Long, Long> entry : dict.entrySet()) {
		     if(entry.getValue() > maxValue) {
		         maxValue = entry.getValue();
		         maxKey = entry.getKey();
		     }
		}	
		
		System.out.println(maxKey + " " + dict.get(maxKey));
		
//		Collection<Integer> lengths = dict.values();
//		int maxLength = Collections.max(lengths);
//		System.out.println(Arrays.asList(lengths).indexOf(maxLength));
		
		
	}
	
	public static Long handle(Long n) {
		Long return_val;
		if (dict.containsKey(n)) {
			return_val = dict.get(n);
			return return_val;
		} else {
			Long m = getCollatzNext(n);
			dict.put(n, 1 + handle(m));
			return dict.get(n);
		}
	}
	
//	public static void handle(int n) {
//		int currVal = 0;
//		int m = n;
//		while (!dict.containsKey(m)) {
//			currVal += 1;
//			m = getCollatzNext(m);
//		} currVal += dict.get(m);
//		dict.put(n, currVal);
//	}	

//	public static void handle(Long n) {
//		Long currVal = 0L;
//		Long m = n;
//		while (!dict.containsKey(m)) {
//			currVal += 1;
//			m = getCollatzNext(m);
//		} currVal += dict.get(m);
//		dict.put(n, currVal);
//	}
	
	public static Long getCollatzNext(Long n) {
		if (n%2==0) {
			return n/2;
		} else {
			return (3*n)+1;
		}
	}
}
