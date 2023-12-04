public class PersonTester {
    public static void main(String[] args) {
        Measurable[] persons = new Measurable[3];

        persons[0] = new Person("Joe", 183);
        persons[1] = new Person("Chrissy", 158);
        persons[2] = new Person("Bobby", 175);

        double avg = Data.average(persons);
        Person max = (Person)Data.max(persons);

        System.out.println("Average height: " + avg);
        System.out.println("Name of tallest person: " + max.getName());
    }    
}
