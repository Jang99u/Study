public class Sphere {
    private double radius;

    public Sphere(double r) {
        radius = r;
    }

    public double sphereVolume() {
       return 4.0 / 3.0 * Math.PI * Math.pow(radius, 3);
    }

    public double sphereSurface() {
       return 4.0 * Math.PI * radius * radius;
    }
}
