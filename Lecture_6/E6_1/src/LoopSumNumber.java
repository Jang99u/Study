import java.util.Scanner;

public class LoopSumNumber {
	   public static void main(String[] args)
	   {	
		  // a. The sum of all even numbers between 2 and 100 (inclusive).
		  int even_sum = 0;
	      for (int x = 2; x <= 100; x = x + 2)
	      {
	    	  even_sum = even_sum + x;
	      }
	      System.out.println("The even sum is " + even_sum);
	      System.out.println();
	      
	      
	      // b. The sum of all squares between 1 and 100 (inclusive).
	      int square_sum = 0;
	      for (int x = 1; x <= 100; x++)
	      {
	    	  square_sum = square_sum + x * x;
	      }
	      System.out.println("The square sum is " + square_sum);
	      System.out.println();
	      
	      
	      //c. The sum of all odd numbers between a and b (inclusive), where a and b are inputs.
	      Scanner in = new Scanner(System.in);

	      System.out.print("Enter a: ");
	      int a = in.nextInt();

	      System.out.print("Enter b: ");
	      int b = in.nextInt();

	      int odd_sum = 0;
	      for (int x = a; x <= b; x++)
	      {
	         if (x % 2 == 1)
	         {
	        	 odd_sum = odd_sum + x;
	         }
	      }
	      System.out.println("The odd sum is " + odd_sum + ".");
	      System.out.println();
	      
	      // d. The sum of all odd digits of an input. (For example, if the input is 12345, the sum would be 1 + 3 + 5 = 9.)
	      System.out.print("Enter an integer number: ");
	      int num = in.nextInt();

	      int digits_sum = 0;

	      while (num > 0)
	      {
	         int digit = num % 10;  // 5 -> 4 -> 3 -> 2 -> 1
	         if (digit % 2 == 1)
	         {
	        	 digits_sum = digits_sum + digit;
	         }
	         num = num / 10;	// 1234 -> 123 -> 12 -> 1 -> 0
	      }

	      System.out.print("The odd digit sum is " + digits_sum + ".");
	      System.out.println();
	      
	   }

}
