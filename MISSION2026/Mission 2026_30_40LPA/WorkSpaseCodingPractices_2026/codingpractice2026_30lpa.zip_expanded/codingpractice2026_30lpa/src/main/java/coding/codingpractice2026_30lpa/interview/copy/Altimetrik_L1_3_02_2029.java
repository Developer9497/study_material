package coding.codingpractice2026_30lpa.interview.copy;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;


public class Altimetrik_L1_3_02_2029 {

	public static void main(String[] args) {
		
		List<Integer>list1 = Arrays.asList(5, 3, 9, 3, 1);
		List<Integer>list2 =  Arrays.asList(4, 9, 1, 7);
		 
		List<Integer> combinedlsit= Stream.concat(list1.stream(),list2.stream())
				.distinct()
				.sorted(Comparator.reverseOrder())
				.collect(Collectors.toList());
		System.out.println(combinedlsit);
		
		
		Map<Integer,Long> freqmap=Stream.concat(list1.stream(),list2.stream())
				.collect(Collectors.groupingBy(i->i,Collectors.counting()));
		
		System.out.println();
		freqmap.forEach((key,value)->System.out.println(key+"="+value));
	
		
	}
	
	
		
	}


