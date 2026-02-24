package coding.codingpractice2026_30lpa.practice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class MargeTwoArrayList {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Integer>list1 = Arrays.asList(5, 3, 9, 3, 1);
		List<Integer>list2 =  Arrays.asList(4, 9, 1, 7);
		
		List<Integer>Com=new ArrayList<>();
		 Com.addAll(list1);
		 Com.addAll(list2);
	List<Integer> ne=	Com.stream().sorted().distinct().collect(Collectors.toList());
		for (Integer integer : ne) {
			System.out.print(integer);
		} 
		System.out.println("");
	Map<Object, Long>mapint=Com.stream()
        .collect(Collectors.groupingBy(
                n -> n,
                Collectors.counting()
       ));
		mapint.forEach((K,V)->System.out.println(K+"="+V));
	for ( Integer integer : Com) {
		System.out.print(integer);
	}	 
	
	}

}
