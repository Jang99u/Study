public class Student extends Person {
    private String major;

    public Student(String name, int birthYear, String major) {
        super(name, birthYear);
        this.major = major;
    }

    public void setMajor(String newMajor) {
        major = newMajor;
    }

    public String getMajor() {
        return major;
    }

    public String toString() {
        String returnString = String.format("Student[super=Person[name=%s,birthYear=%d],major=%s]", super.getName(), super.getBirthYear(), major);
        return returnString;
    }
}
