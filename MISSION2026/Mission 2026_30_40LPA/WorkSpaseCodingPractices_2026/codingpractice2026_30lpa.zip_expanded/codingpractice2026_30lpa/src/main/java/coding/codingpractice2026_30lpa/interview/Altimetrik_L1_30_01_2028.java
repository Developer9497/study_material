package coding.codingpractice2026_30lpa.interview;

import java.util.HashMap;
import java.util.Map;

import ch.qos.logback.core.rolling.LengthCounter;


public class Altimetrik_L1_30_01_2028 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//List<>stringlist = new
		//System.out.println(lenghtoflogeststr("pwwkew") );
		System.out.println(lenghtoflogeststr("abcabcbb") );
		
		
		//System.out.println(lenghtoflogeststr("bbbbb") );
		//bbbbb
		

	}
	
	public static int lenghtoflogeststr(String s) {
		
//		Set<Character> set=new HashSet<>();
//		int start=0,maxlen=0;
//		for (int i = 0; i < s.length(); i++) {
//			while(set.contains(s.charAt(i))) {
//				set.remove(s.charAt(start++));
//			}
//			set.add(s.charAt(i));
//			
//			maxlen=Math.max(maxlen, i-start+1);
//			
//			
//		}
//	System.out.println();
//		for (Character character : set) {
//			System.out.print(character);
//		}
		int maxLength=0, strat=0;
		Map<Character,Integer> CharIndex=new HashMap<>();
		for (int i=0;i<s.length();i++) {
			char c=s.charAt(i);
			if(CharIndex.containsKey(c)) {
				maxLength=Math.max(maxLength, i-strat+1);
				CharIndex.put(c, i);
			}
			maxLength=Math.max(maxLength, i-strat+1);
			CharIndex.put(c, i);
		}
				
		
		
	return maxLength;

//		return IntStream.range(0,s.length())
//				.mapToObj(strat-> IntStream.range(strat, s.length())
//						.map(end->s.substring(strat, end+1))
//						.filter(sub->sub.chars().distinct().count()==sub.length())
//						.max((a,b)->Integer.compare(a.lenght(),b.lenght())))
//				.flatMap(Optional :: stream)
//				.map(String ::lenght).max(Integer ::compare)
//				.orElse(0);
//				
				
				
				
				
		
	}

}
