package coding.codingpractice2026_30lpa.practice;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class StringCompression {
    public static void main(String[] args) {

        String s = "aaabbc";
        StringBuilder result = new StringBuilder();
        int count = 1;

//        for(int i=1;i<=s.length();i++){
//            if(i < s.length() && s.charAt(i)==s.charAt(i-1)){
//                count++;
//            } else {
//                result.append(s.charAt(i-1)).append(count);
//                count = 1;
//            }
//        }
        Map<Object, Long> maodat=new HashMap<>();
for(Character ch:s.toCharArray()) {
	maodat.put(ch,maodat.getOrDefault(ch,(long) 0)+1);
}
maodat.forEach((k, v) -> System.out.print(k+""+v));
        System.out.println();
    }
}
