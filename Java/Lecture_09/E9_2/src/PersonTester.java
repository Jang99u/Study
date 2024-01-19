public class PersonTester {
    public static void main(String[] args) {
        Person p = new Person("Perry", 1959);
        Student s = new Student("Sylvia", 1979, "Computer Science");
        Instructor e = new Instructor("Edgar", 1969, 65000);
        System.out.println(p);
        System.out.println(s);
        System.out.println(e);
    }
}
