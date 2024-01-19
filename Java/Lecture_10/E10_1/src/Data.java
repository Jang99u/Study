public class Data {
    public static double average(Measurable[] object) {
        double heightSum = 0;
        int size = 0;
        double avg;

        for(Measurable obj : object) {
            heightSum += obj.getMeasure();
            size ++;
        }
        avg = heightSum / size;

        return avg;
    }

    public static Measurable max(Measurable[] object) {
        double heightMax = 0;
        Measurable maxVal = null;

        for(Measurable obj : object) {
            if(heightMax < obj.getMeasure()) {
                maxVal = obj;
                heightMax = obj.getMeasure();
            }
        }

        return maxVal;
    }
}