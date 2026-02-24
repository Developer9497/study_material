package coding.codingpractice2026_30lpa.practice;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class EvenIndexUppercaseStream {
    public static void main(String[] args) {

        String s = "javabasics";

        String result = IntStream.range(0, s.length())
                .mapToObj(i -> i % 2 == 0 
                        ? Character.toUpperCase(s.charAt(i)) 
                        : s.charAt(i))
                .map(String::valueOf)
                .collect(Collectors.joining());

        System.out.println(result);
    }
}
