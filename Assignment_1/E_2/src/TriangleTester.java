import java.util.Scanner;

public class TriangleTester {
    public static void main(String[] args) {
        Scanner keyIn = new Scanner(System.in);

        System.out.print("Vertex x1? ");
        double x1 = keyIn.nextDouble();
        System.out.print("Vertex y1? ");
        double y1 = keyIn.nextDouble();
        System.out.print("Vertex x2? ");
        double x2 = keyIn.nextDouble();
        System.out.print("Vertex y2? ");
        double y2 = keyIn.nextDouble();
        System.out.print("Vertex x3? ");
        double x3 = keyIn.nextDouble();
        System.out.print("Vertex y3? ");
        double y3 = keyIn.nextDouble();

        Triangle myTriangle = new Triangle(x1, y1, x2, y2, x3, y3);
        myTriangle.printXY();
        myTriangle.printLengthAngle();
        myTriangle.printPerimeterArea();
    }
}
