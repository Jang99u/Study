import java.awt.Rectangle;

public class Rectangles42 {
    public static void main(String[] args) {
        Rectangle r1 = new Rectangle(0, 0, 3, 14);
        Rectangle r2 = new Rectangle(0, 0, 10, 11);

        System.out.println("R1 Height: " + r1.getHeight());
        System.out.println("R1 Width: " + r1.getWidth());
        System.out.println("R2 Height: " + r2.getHeight());
        System.out.println("R2 Width: " + r2.getWidth());
    }
}