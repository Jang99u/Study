public class Triangle {
    private double x1;
    private double y1;
    private double length1;
    private double angle1;
    private double x2;
    private double y2;
    private double length2;
    private double angle2;
    private double x3;
    private double y3;
    private double length3;
    private double angle3;

    public Triangle(double X1, double Y1, double X2, double Y2, double X3, double Y3) {
        x1 = X1;
        y1 = Y1;
        x2 = X2;
        y2 = Y2;
        x3 = X3;
        y3 = Y3;

        length1 = Math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3)); 
        length2 = Math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3)); 
        length3 = Math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)); 

        angle1 = getAngle(x2-x1, y2-y1, x3-x1, y3-y1);
        angle2 = getAngle(x1-x2, y1-y2, x3-x2, y3-y2);
        angle3 = getAngle(x1-x3, y1-y3, x2-x3, y2-y3);
    }

    private double getAngle(double a1, double a2, double b1, double b2) {
        double dotProduct = a1*b1 + a2*b2;
        double size = Math.sqrt(a1*a1 + a2*a2) * Math.sqrt(b1*b1 + b2*b2);
        size = Math.floor(size * 10000) / 10000.0;
        double theta = Math.acos(size / dotProduct);
        return theta;
    }

    private double getPerimeter() {
        return length1 + length2 + length3;
    }

    private double getArea() {
        return (1/2) * (x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3);
    }

    public void printXY() {
        System.out.println("---------------------");
        System.out.println("| index |  x  |  y  |");
        System.out.println("---------------------");
        System.out.printf("|   1   | %.2f| %.2f|\n", x1, y1);
        System.out.println("---------------------");
        System.out.printf("|   2   | %.2f| %.2f|\n", x2, y2);
        System.out.println("---------------------");
        System.out.printf("|   3   | %.2f| %.2f|\n", x3, y3);
        System.out.println("---------------------\n");
    }

    public void printLengthAngle() {
        System.out.println("--------------------------");
        System.out.println("| index | length | angle |");
        System.out.println("--------------------------");
        System.out.printf("|   1   |    %.2f|   %.2f|\n", length1, angle1);
        System.out.println("--------------------------");
        System.out.printf("|   2   |    %.2f|   %.2f|\n", length2, angle2);
        System.out.println("--------------------------");
        System.out.printf("|   3   |    %.2f|   %.2f|\n", length3, angle3);
        System.out.println("--------------------------\n");
    }

    public void printPerimeterArea() {
        System.out.println("--------------------");
        System.out.println("| perimeter | Area |");
        System.out.println("--------------------");
        System.out.printf("| %10.2f|  %4.2f|\n", getPerimeter(), getArea());
        System.out.println("--------------------");
    }
}