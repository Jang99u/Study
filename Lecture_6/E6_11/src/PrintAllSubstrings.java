import java.util.Scanner;

public class PrintAllSubstrings
{
    public static void main(String[] args)
    {
        Scanner keyIn = new Scanner(System.in);
        System.out.println("Enter a word: ");
        String word = keyIn.next();

        for(int i = word.length(); i >= 1; i--) {
            for(int j = 0; j < i; j++) {
                int start = j;
                int end = j+(word.length()-i+1);
                System.out.println(word.substring(start, end));
            }
        }

        keyIn.close();
    }
}