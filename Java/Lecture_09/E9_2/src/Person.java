public class Person {
    private String name;
    private int birthYear;

    public Person(String name, int birthYear) {
        this.name = name;
        this.birthYear = birthYear;
    }

    public void setName(String newName) {
        name = newName;
    }
    
    public void setBirth(int newBirth) {
        birthYear = newBirth;
    }

    public String getName() {
        return name;
    }

    public int getBirthYear() {
        return birthYear;
    }

    public String toString() {
        String returnString = String.format("Person[name=%s,birthYear=%d]", name, birthYear);
        return returnString;
    }
}
