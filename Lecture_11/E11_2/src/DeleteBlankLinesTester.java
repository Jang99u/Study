import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import E11_2.BlankLinesRemover;

public class DeleteBlankLinesTester {
    public static void main(String[] args) {
        BlankLinesRemover.removeLines("lines.txt");
        int count = 0;
        try(Scanner in = new Scanner(new File("lines.txt"))) {
            while(in.hasNextLine()) {
                in.nextLine();
                count++;
            }
        } catch(FileNotFoundException e) {
            e.printStackTrace();
        }
        System.out.println("Number of non-blank lines: " + count);
    }
}