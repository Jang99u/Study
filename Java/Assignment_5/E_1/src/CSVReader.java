import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

/**
 * CSVReader 클래스는 CSV파일을 읽어와 2차원 ArrayList에 저장하는 클래스입니다.
 */
public class CSVReader {
    private ArrayList<ArrayList<String>> csvMatrix; 

    /**
     * CSVReader 클래스의 기본 생성자입니다. CSVReader 객체를 초기화합니다.
     */
    public CSVReader() {
        csvMatrix = new ArrayList<ArrayList<String>>();
    }

    /**
     * 파일을 읽어와 2차원 ArrayList에 저장하는 method입니다.
     * 파일을 읽고 한 줄씩 읽어와 쉼표를 구분으로 나눈 뒤 한 줄씩 저장해줍니다.
     * 
     * @param fileName 읽어올 파일 명
     * @throws FileNotFoundException 해당 파일이 없을 시 상위 method로 쏘는 exception
     */
    public void readFile(String fileName) throws FileNotFoundException {
        File inputFile = new File(fileName);
        Scanner in = new Scanner(inputFile);

        while(in.hasNextLine()) {
            ArrayList<String> lineArr = new ArrayList<String>();
            String line = in.nextLine();
            String[] linearr = line.split(",");
            for(String l : linearr) {
                if(l.charAt(0) == '\"') l = l.substring(1, l.length()-1);
                lineArr.add(l);
            }
            csvMatrix.add(lineArr);
        }

        in.close();
    }

    /**
     * 읽어온 파일의 행수를 구해주는 method입니다. 
     * 
     * @return 행의 수
     */
    public int numberOfRows() {
        return csvMatrix.size();
    }

    /**
     * 읽어온 파일의 열수를 구해주는 method입니다.
     * 
     * @param row 열의 수를 확인할 행
     * @return 열의 수
     */
    public int numberOfFields(int row) {
        return csvMatrix.get(row).size();
    }

    /**
     * 행과 열을 입력받아, 해당 index에 어떤 원소가 있는지 String 형태로 반환해주는 함수입니다.
     * 
     * @param row 참조할 행 index
     * @param column 참조할 열 index
     * @return 양식에 맞게 원소값을 String 형태로 return
     */
    public String field(int row, int column) {
        String value = csvMatrix.get(row-1).get(column-1);
        return "Row " + row + ", " + "Col " + column + ": " + value;
    }
}