import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class RowsOfNumbers {
    public static void main(String[] args) throws FileNotFoundException { 
        System.out.println("This program reads variable-length lines of numbers from a file 'data.txt'");
        System.err.println("and prints the line along with average.");
        File inFile = new File("data.txt");
        Scanner in = new Scanner(inFile);
        int rowNumber = 1;
        while(in.hasNextLine()) {
            String input = in.nextLine();
            if(input == "") {
                System.out.println("Row " + rowNumber + ":        " + "average is 0.0");
                rowNumber += 1;
            } else {
                String[] numberstr = input.split(" ");
                double[] numbers = new double[numberstr.length];
                double numSum = 0;
                int count = 0;

                for(int i = 0; i < numberstr.length; i++) {
                    numbers[i] = Double.parseDouble(numberstr[i]);
                }

                System.out.print("Row " + rowNumber + ":    ");

                for(double i : numbers) {
                    System.out.print(i + " ");
                    numSum += i;
                    count += 1;
                }
                System.out.println("    average is " + (numSum / count));
                rowNumber += 1;
            }
        }
        in.close();
    }
}