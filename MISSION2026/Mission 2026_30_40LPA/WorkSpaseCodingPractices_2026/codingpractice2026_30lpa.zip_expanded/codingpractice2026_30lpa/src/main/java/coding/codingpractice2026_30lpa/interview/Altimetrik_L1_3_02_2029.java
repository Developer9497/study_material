package coding.codingpractice2026_30lpa.interview;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;


public class Altimetrik_L1_3_02_2029 {

	public static void main(String[] args) {
		
	String input="aaabbaaaacccccbbbcc";
	

			
			input.chars().mapToObj(c->(char)c)
			.collect(Collectors.groupingBy(c->c,Collectors.counting()))
			.forEach((k,v)->System.out.println(k+"="+v));
	
	
	
	
	
	System.out.println("-------------------------------");
	
	
		 int count=1;
	//	output= a=4	b=3 c=5
		 Map<Character,Integer> map=new HashMap<>();
	for(int i=1;i<input.length();i++){
		
		if(input.charAt(i)==input.charAt(i-1)) {
			count++;
		
		}else {
			char ch=input.charAt(i-1);
			map.put(ch,Math.max(map.getOrDefault(ch,0),count));
			count=1;
				
		}
	}
	char last=input.charAt(input.length()-1);
	map.put(last,Math.max(map.getOrDefault(last,0),count));
	map.forEach((k,v)->System.out.println(k+"="+v));
	}
	
	
		
	}


