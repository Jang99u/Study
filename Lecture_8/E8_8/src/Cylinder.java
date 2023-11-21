public class Cylinder {
    private double radius;
    private double height;

    public Cylinder(double r, double h) {
        radius = r;
        height = h;
    }

    public double cylinderVolume() {
       return Math.PI * radius * radius * height;
    }

    public double cylinderSurface() {
       return 2 * Math.PI * radius * (radius + height);
    }
}
