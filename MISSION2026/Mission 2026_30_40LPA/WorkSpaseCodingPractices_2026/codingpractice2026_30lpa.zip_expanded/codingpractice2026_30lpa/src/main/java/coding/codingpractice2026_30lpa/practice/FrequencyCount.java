package coding.codingpractice2026_30lpa.practice;

import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class FrequencyCount {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
String s="javabasics";
 usingstream(s);
 basicaproch(s);
 withousuingcollection(s);
	}

	private static void basicaproch(String s) {
		// TODO Auto-generated method stub
		System.out.println("using collection");
		Map<Character,Integer> mapdata=new HashMap<>();
		char[]c=s.toCharArray();
		for(int i=0;i<s.length();i++) {
			mapdata.put(c[i],mapdata.getOrDefault(c[i], 0)+1);
			
			
		}
		//mapdata.forEach((k,v)->System.err.println(k+"="+v));
		System.out.println(mapdata);
		
	}

	private static void usingstream(String s) {
		System.out.println("using steram api");
		// TODO Auto-generated method stub
		Map<Character,Long> mapdata=s.chars()
				.mapToObj(c-> (char) c).collect(Collectors
						.groupingBy(ch->ch,Collectors.counting()));
		System.out.println(mapdata);
	}
	
	    public static void withousuingcollection(String s) {
System.out.println("without using collection");
	        
	        for(int i=0; i<s.length(); i++) {
	            char ch = s.charAt(i);
	            int count = 0;

	            for(int j=0; j<s.length(); j++) {
	                if(s.charAt(j) == ch) {
	                    count++;
	                }
	            }

	            if(s.indexOf(ch) == i) { // print only first occurrence
	                System.out.print(ch + "=" + count+",");
	            }
	        }
	    }
	


}
