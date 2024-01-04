package E11_2;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.ArrayList;

public class BlankLinesRemover {
    public static void removeLines(String fileName) {
        ArrayList<String> lines = new ArrayList<>();
        try(Scanner in = new Scanner(new File(fileName))) {
            while(in.hasNextLine()) {
                String inputLine = in.nextLine();
                if(inputLine == "") continue; 
                else lines.add(inputLine);
            }
        } catch(FileNotFoundException e) {
            e.printStackTrace();
        }

        for(String line : lines) {
            System.out.println(line);
        }

        try(PrintWriter out = new PrintWriter("lines.txt")) {
            for(String line : lines) {
                out.println(line);
            }
        } catch(FileNotFoundException e) {
            e.printStackTrace();
        }
    }    
}