import java.util.Scanner;

public class Input {
    public static int readInt(Scanner in, String prompt, String error, int min, int max) {
        System.out.println(prompt);
        int age = in.nextInt();

        while(age < min || age > max) {
            System.out.println(error);    
            System.out.println(prompt);
            age = in.nextInt();
        }
        
        return age;
    }
}