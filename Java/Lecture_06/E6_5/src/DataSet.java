public class DataSet {
    private double sum;
    private int n;
    private double largestValue;
    private double smallestValue;
    private final int INF = 2000000000;

    public DataSet() {
        largestValue = INF * -1;
        smallestValue = INF;
    }

    public void add(double x) {
        sum += x;
        n += 1;
        largestValue = Math.max(largestValue, x);
        smallestValue = Math.min(smallestValue, x);
    }

    public double getAverage() {
        return sum / n;
    }

    public double getSmallest() {
        return smallestValue;
    }

    public double getLargest() {
        return largestValue;
    }

    public double getRange() {
        return largestValue - smallestValue;
    }

    public int getCount() {
        return n;
    }
}