public class Instructor extends Person {
    private double salary;

    public Instructor(String name, int birthYear, double salary) {
        super(name, birthYear);
        this.salary = salary;
    }

    public void setSalary(double newSalary) {
        salary = newSalary;
    }

    public double getMajor() {
        return salary;
    }

    public String toString() {
        String returnString = String.format("Instructor[super=Person[name=%s,birthYear=%d],major=%.1f]", super.getName(), super.getBirthYear(), salary);
        return returnString;
    }
}
