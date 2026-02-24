package coding.codingpractice2026_30lpa.practice;

public class Reverse_an_Array {
	 public static void main(String[] args) {

	        // Create object of class to call non-static methods
		 Reverse_an_Array obj = new Reverse_an_Array();

	        // Call basic approach method
	        obj.usingBasicApproach();

	        // Call Stream API approach method
	        obj.usingStreamApi();
	    }

	private void usingStreamApi() {
		// TODO Auto-generated method stub
		int[] arr = {1, 2, 3, 4, 5};
		int left = 0, right = arr.length - 1;

		while (left < right) {
		    int temp = arr[left];
		    arr[left] = arr[right];
		    arr[right] = temp;
		    left++;
		    right--;
		}

		// print reversed array
		for (int num : arr) {
		    System.out.print(num + " ");
		}
		System.out.println();
	}
	private void usingBasicApproach() {
		// TODO Auto-generated method stub
		int[] arr = {1, 2, 3, 4, 5};
		int[] rev = new int[arr.length];

		for (int i = 0; i < arr.length; i++) {
		    rev[i] = arr[arr.length - 1 - i];
		}
System.out.println("\n");
for (int i : rev) {
	System.out.print(i);
}
	}
}

