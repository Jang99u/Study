public class Quiz implements Measurable{
    private double score;
    private String grade;

    public Quiz(double score, String grade) {
        this.score = score;
        this.grade = grade;
    }

    public double getMeasure() {
        return score;
    }

    public String getGrade() {
        return grade;
    }
}
