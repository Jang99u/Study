import java.util.Scanner;

public class SequenceOfValues {
    public static void main(String[] args) {
        Scanner keyIn = new Scanner(System.in);
        DataSet data = new DataSet();

        System.out.print("Enter a set of floating-point values. ");
        System.out.println("Enter anything other than a number to indicate the end of the series:  ");

        while(keyIn.hasNextDouble()) {
            data.add(keyIn.nextDouble());
        }

        System.out.printf("The average of the value is: %.6f\n", data.getAverage());
        System.out.printf("The smallest value is: %.6f\n", data.getSmallest());
        System.out.printf("The largest value is: %.6f\n", data.getLargest());
        System.out.printf("The range is: %.6f\n", data.getRange());
    
        keyIn.close();
   }
}
