import java.awt.Rectangle;

public class PerimeterTester {
    public static void main(String[] args) {
        Rectangle r1 = new Rectangle(0, 0, 25, 25);
        double perimeter = (r1.getWidth() * 2) + (r1.getHeight() * 2);

        System.out.println("Perimeter: " + perimeter);
    }
}