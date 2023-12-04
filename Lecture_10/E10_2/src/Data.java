public class Data {
    public static double average(Measurable[] object) {
        double scoreSum = 0;
        int size = 0;

        for(Measurable obj : object) {
            scoreSum += obj.getMeasure();
            size++;
        }
        double avg = scoreSum / size;

        return avg;
    }

    public static Measurable max(Measurable[] object) {
        double maxScore = 0;
        Measurable maxVal = null;

        for(Measurable obj : object) {
            if(maxScore < obj.getMeasure()) {
                maxVal = obj;
                maxScore = obj.getMeasure();
            }
        }

        return maxVal;
    }
}
