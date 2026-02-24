package coding.codingpractice2026_30lpa.practice;
import java.util.*;

public class LongestSubstring {
    public static void main(String[] args) {

        //String s = "abcabcbb";
    	String s="kirankale";
        Set<Character> set = new LinkedHashSet();

        int left = 0, maxLength = 0;

        for (int right = 0; right < s.length(); right++) {

            while(set.contains(s.charAt(right))) {
            	//System.out.println(s.charAt(right));
                set.remove(s.charAt(left));
                //System.out.println(set);
                left++;
            }

            set.add(s.charAt(right));
            System.out.println(set);
            maxLength = Math.max(maxLength, right - left + 1);
        }

        System.out.println("Max Length: " + maxLength);
    }
}
