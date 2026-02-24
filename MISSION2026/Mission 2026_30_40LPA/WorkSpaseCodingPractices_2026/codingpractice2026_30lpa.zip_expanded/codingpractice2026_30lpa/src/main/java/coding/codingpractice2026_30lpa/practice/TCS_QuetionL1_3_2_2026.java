package coding.codingpractice2026_30lpa.practice;

import java.util.Iterator;

public class TCS_QuetionL1_3_2_2026 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
String input ="ooo4bb2cc4";
StringBuilder sb=new StringBuilder();

   for (char c :input.toCharArray()) {
	   if(Character.isLetter(c)) {
		   sb.append(c);
		   
	   }else if (Character.isDigit(c)) {
		   int count =c-'0';
		   int count2=Integer.parseInt(String.valueOf(c));
System.err.println(c+4+"="+count);
		   for (int i = 0; i < count; i++) {
               System.out.println(sb);
           }
		   sb.setLength(0);
		
	}
	   
   }
	}

}
