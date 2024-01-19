public class HybridCar {
    private double carCost;
    private double milePerYear;
    private double gasCost;
    private double efficiency;
    private double reSaleValue;

    public HybridCar(double cCost, double mile, double gCost, double effi, double reSale) {
        carCost = cCost;
        milePerYear = mile;
        gasCost = gCost;
        efficiency = effi;
        reSaleValue = reSale;
    }

    public double getValue() {
        return carCost + ((milePerYear / efficiency) * gasCost * 5) - reSaleValue;
    }
}
