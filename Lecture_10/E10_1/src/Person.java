public class Person implements Measurable {
    private String name;
    private double height;

    public Person() {
        name = "";
        height = 0;
    }

    public Person(String name, double height) {
        this.name = name;
        this.height = height;
    }

    public String getName() {
        return name;
    }

    public double getMeasure() {
        return height;
    }
}
