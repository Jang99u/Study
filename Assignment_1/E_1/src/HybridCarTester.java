import java.util.Scanner;

public class HybridCarTester {
    public static void main(String[] args) {
        Scanner keyIn = new Scanner(System.in);

        System.out.print("What was the cost of the car? ");
        double cCost = keyIn.nextDouble();
        System.out.print("How many miles per year will you drive the car? ");
        double mile = keyIn.nextDouble();
        System.out.print("What is the cost of a gallon of gas? ");
        double gCost = keyIn.nextDouble();
        System.out.print("How many miles per gallon does the car average? ");
        double effi = keyIn.nextDouble();
        System.out.print("What was the resale value of the car after five years? ");
        double reSale = keyIn.nextDouble();

        HybridCar myCar = new HybridCar(cCost, mile, gCost, effi, reSale);
        System.out.print("The total cost of ownership is " + myCar.getValue());
    }
}
