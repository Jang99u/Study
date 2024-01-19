public class QuizTester {
    public static void main(String[] args) {
        Measurable[] quizData = new Measurable[3];
        quizData[0] = new Quiz(89, "B+");
        quizData[1] = new Quiz(90, "A-");
        quizData[2] = new Quiz(73, "C");

        double avg = Data.average(quizData);
        Quiz max = (Quiz) Data.max(quizData);

        System.out.println("Average score: " + avg);
        System.out.println("Highest score: " + max.getMeasure());
        System.out.println("Highest grade: " + max.getGrade());
    }   
}