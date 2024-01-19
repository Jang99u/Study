import java.util.Scanner;

public class GeometryDemo {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter radius: ");
        double radius = in.nextDouble();
        System.out.println("Enter height: ");
        double height = in.nextDouble();

        Cone myCone = new Cone(radius, height);
        Sphere mySphere = new Sphere(radius);
        Cylinder myCylinder = new Cylinder(radius, height);

        System.out.printf("Sphere volume: %.2f\n", mySphere.sphereVolume());
        System.out.printf("Sphere surface: %.2f\n", mySphere.sphereSurface());
        System.out.printf("Cylinder volume: %.2f\n", myCylinder.cylinderVolume());
        System.out.printf("Cylinder surface: %.2f\n", myCylinder.cylinderSurface());
        System.out.printf("Cone volume: %.2f\n", myCone.coneVolume());
        System.out.printf("Cone surface: %.2f\n", myCone.coneSurface());

        in.close();
    }
}