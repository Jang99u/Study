public class Counter {
    private int value;
    private int max;

    public void setLimit(int maximum)
    {
        max = maximum;
    }

    public int getValue()
    {
        return value;
    }

    public void click()
    {
        value += 1;
        value = Math.min(value, max);
    }

    public void reset()
    {
        value = 0;
    }
}
