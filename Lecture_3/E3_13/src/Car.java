public class Car {
    private double gas;
    private double efficiency;

    public Car(double anEfficiency)
    {
        efficiency = anEfficiency;
    }

    public void addGas(double amount)
    {
        gas += amount;
    }

    public void drive(double distance)
    {
        gas -= distance / efficiency;
    }

    public double getGasInTank()
    {
        return gas;
    }
}
