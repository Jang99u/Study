class Employee
{
    private String name;
    private double baseSalary;

    public Employee() {
       name = "";
       baseSalary = 0.00;
    } 

    public Employee(String name, double baseSalary) {
       this.name = name;
       this.baseSalary = baseSalary;
    }

    public void setName(String newName)
    {
        name = newName;
    }

    public void setBaseSalary(double newSalary)
    {
        baseSalary = newSalary;
    }

    public String getName()
    {
        return name;
    }

    public double getSalary()
    {
        return baseSalary;
    }
}

class Manager extends Employee
{
    private double bonus;

    public Manager(String newName, double newSalary, double newBonus)
    {
        super(newName,newSalary);
        /* 
        setName(newName);
        setBaseSalary(newSalary);
        */
        bonus = newBonus;
    }

    public double getBonus()
    {
        return bonus;
    }

    public void setBonus(double bonus)
    {
        this.bonus = bonus;
    }

}

public class EmployeeTest
{
    public static void main(String[] args)
    {
        // Create an employee
        Employee employee = new Employee();
        employee.setName("James Garfield");
        employee.setBaseSalary(23000.00);
        Manager manager = new Manager("Mary Wilson", 25000, 3000);
        System.out.printf("Employee %s makes $%.2f.\n", employee.getName(), employee.getSalary());
        System.out.printf("Manager %s makes $%.2f and a bonus of $%.2f.\n", manager.getName(), manager.getSalary(), manager.getBonus());

    }

}

