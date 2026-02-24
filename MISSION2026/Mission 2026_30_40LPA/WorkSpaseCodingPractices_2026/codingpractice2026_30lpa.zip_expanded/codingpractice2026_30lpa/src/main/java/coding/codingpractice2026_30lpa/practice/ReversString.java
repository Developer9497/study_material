//package coding.codingpractice2026_30lpa.practice;
//
//import java.util.stream.Collectors;
//import java.util.stream.IntStream;
//
//public class ReverseString {
//
//    public static void main(String[] args) {
//
//        // Create object of class to call non-static methods
//        ReverseString obj = new ReverseString();
//
//        // Call basic approach method
//        obj.usingBasicApproach();
//
//        // Call Stream API approach method
//        obj.usingStreamApi();
//    }
//
//    // 1️⃣ Reverse string using basic loop approach
//    public void usingBasicApproach() {
//
//        // Original string
//        String str = "hello";
//
//        // Empty string to store reversed result
//        String rev = "";
//
//        // Loop starts from last index (length - 1)
//        // Because string index starts from 0
//        for (int i = str.length() - 1; i >= 0; i--) {
//
//            // charAt(i) returns character at index i
//            // Append each character to rev string
//            rev += str.charAt(i);
//        }
//
//        // Print original and reversed string
//        System.out.println("Original String = " + str);
//        System.out.println("Result (Basic Approach) = " + rev);
//    }
//
//    // 2️⃣ Reverse string using Java Stream API
//    public void usingStreamApi() {
//
//        // Original string
//        String str = "hello";
//
//        /*
//         * IntStream.range(0, str.length())
//         * → generates numbers from 0 to length-1
//         *
//         * str.length() - 1 - i
//         * → accesses characters from the end of string
//         *
//         * mapToObj(...)
//         * → converts index to character
//         *
//         * map(String::valueOf)
//         * → converts character to String
//         *
//         * Collectors.joining()
//         * → joins all characters into one string
//         */
//        String rev = IntStream.range(0, str.length())
//                .mapToObj(i -> str.charAt(str.length() - 1 - i))
//                .map(String::valueOf)
//                .collect(Collectors.joining());
//
//        // Print original and reversed string
//        System.out.println("Original String = " + str);
//        System.out.println("Result (Stream API) = " + rev);
//    }
//}
