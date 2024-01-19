import java.util.Scanner;

/**
 * TerrainTester 클래스는 Terrain 클래스가 정상적으로 작동하는지 보기 위한 Tester 클래스입니다.
 */
public class TerrainTester {
    /**
     * 사용자로부터 2차원 배열 형태로 값을 입력받고 저장합니다.
     * 저장된 2차원 배열은 생성자로 들어가고, 이 후 객체 내 method들이 정상적으로 작동되는 지 확인합니다.
     * 
     * @param args 지역의 고도를 외부로부터 받기 위한 문자열 인자
     */
    public static void main(String[] args) {
        double[][] territory = new double[10][10];
        Scanner keyIn = new Scanner(System.in);

        System.out.println("Enter height values");
        for(int i = 0; i < 10; i++) {
            for(int j = 0; j < 10; j++) {
                double num = keyIn.nextDouble();
                territory[i][j] = num;
            }
        }

        Terrain terrain = new Terrain(territory);
        double[] interval = new double[10];
        double maxval = terrain.getMaxHeight();
        double minval = terrain.getMinHeight();
        double diff = (maxval - minval) / 9;
        for(int i = 0; i < 10; i++) {
            interval[i] = minval + (diff * i);
        }

        System.out.println("Lower Height: " + minval);
        System.out.println("Highest Height: " + maxval);
        for(int i = 0; i < 10; i++) {
            double level = interval[i];
            terrain.printFloodMap(level);
        }

        keyIn.close();
    }
}
