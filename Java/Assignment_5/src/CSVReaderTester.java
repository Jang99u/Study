import java.io.FileNotFoundException;

/**
 * CSVReaderTester 클래스는 CSVReader 클래스가 정상적으로 작동하는지 보기 위한 Tester 클래스입니다.
 */
public class CSVReaderTester {
    /**
     * CSVReader 클래스의 객체의 param으로 파일명을 넣어줍니다.
     * 해당 파일이 없다면 에러메시지를 출력하고 프로그램을 종료합니다.
     * 해당 파일이 존재한다면 양식에 맞게 여러 정보를 출력합니다.
     * 
     * @param args
     */
    public static void main(String[] args) {
        CSVReader myCSV = new CSVReader();
        try {
            myCSV.readFile("att2020.csv");
        } catch (FileNotFoundException exception) {
            System.out.print(exception.getMessage());
            return;
        }

        System.out.println("Number of rows: " + myCSV.numberOfRows());
        System.out.println("Expected: 214");
        System.out.println();
        System.out.println("Number of fields in one row: " + myCSV.numberOfFields(0));
        System.out.println("Expected: 7");
        System.out.println();
        System.out.println(myCSV.field(10, 1));
        System.out.println("Expected: 3/12/2020");
        System.out.println();
        System.out.println(myCSV.field(10, 2));
        System.out.println("Expected: 24.87");
        System.out.println();
        System.out.println(myCSV.field(10, 3));
        System.out.println("Expected: 24.95");
        System.out.println();
        System.out.println(myCSV.field(10, 4));
        System.out.println("Expected: 24.87");
        System.out.println();
        System.out.println(myCSV.field(10, 5));
        System.out.println("Expected: 24.95");
        System.out.println();
        System.out.println(myCSV.field(10, 6));
        System.out.println("Expected: 217500");
        System.out.println();
        System.out.println(myCSV.field(10, 7));
        System.out.println("Expected: average: \"22.64\"");
        System.out.println();
    }    
}
