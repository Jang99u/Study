public class Cone {
    private double radius;
    private double height;
    
    public Cone(double r, double h) {
        radius = r;
        height = h;
    }

    public double coneVolume() {
       return 1.0 / 3.0 * Math.PI * radius * radius * height;
    }

    public double coneSurface() {
       return Math.PI * radius * radius + Math.PI * radius * Math.sqrt(radius * radius + height * height);
    }
}