package coding.codingpractice2026_30lpa.practice;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Iterator;

public class AnagramCheck2 {
    public static void main(String[] args) {

        String s1 = "listenl";
        String s2 = "silent";

        char[] a = s1.toCharArray();
        char[] b = s2.toCharArray();

        Arrays.sort(a);
        Arrays.sort(b);
        System.out.println("a=");
        for(char c:a) {
        	 System.out.print(c);
        	
        }
        System.out.println();
        System.out.println("b=");
        for(char c:b) {
       	
       	System.out.print(c);
       }
        System.out.println();
        if (Arrays.equals(a, b)) {
            System.out.println("Anagram");
        } else {
            System.out.println("Not Anagram");
        }
    }
}
