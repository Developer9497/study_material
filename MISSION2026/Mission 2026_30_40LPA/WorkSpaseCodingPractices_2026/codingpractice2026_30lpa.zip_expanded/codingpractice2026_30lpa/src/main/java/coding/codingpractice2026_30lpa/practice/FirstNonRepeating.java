package coding.codingpractice2026_30lpa.practice;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class FirstNonRepeating {
    public static Character firstNonRepeatingChar(String input) {

        Map<Character, Long> frequencyMap =
                input.chars()
                     .mapToObj(c -> (char) c)
                     .collect(Collectors.groupingBy(
                             Function.identity(),
                             LinkedHashMap::new,
                             Collectors.counting()
                     ));

        return frequencyMap.entrySet()
                .stream()
                .filter(entry -> entry.getValue() == 1)
                .map(Map.Entry::getKey)
               
                .findFirst()
                .orElse(null);
    }

    public static void main(String[] args) {
        String str = "stress";
        System.out.println("First non-repeating character: " + firstNonRepeatingChar(str));
       
        System.out.println( isPalindrome(str));
    }
    
    public static boolean isPalindrome(String s) {

        String cleaned = s.chars()
                .filter(Character::isLetterOrDigit)   // remove special chars
                .mapToObj(c -> String.valueOf((char) c).toLowerCase())
                .collect(Collectors.joining());

        return IntStream.range(0, cleaned.length() / 2)
                .allMatch(i -> cleaned.charAt(i) == cleaned.charAt(cleaned.length() - 1 - i));
    }

}
