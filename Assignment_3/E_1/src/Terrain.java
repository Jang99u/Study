/**
 * Terrain 클래스는 입력받은 지역의 최저고도, 최고고도, 홍수여부 등을 판별해주는 클래스 입니다.
 */
public class Terrain {
    public static final double INF = 100000000;
    private double[][] area = new double[10][10];

    /**
     * Terrain 클래스의 기본 생성자입니다. Terrain 객체를 초기화합니다.
     * 
     * @param heights 지역의 각 index별 고도가 적혀있는 2차원 배열
     */
    public Terrain(double[][] heights) {
        area = heights;
    }

    /**
     * 2차원 배열 area중 가장 작은 값. 즉, 최저고도를 찾는 method입니다. 
     * 
     * @return area중 가장 작은 값
     */
    public double getMinHeight () {
        double minHeight = INF;
        for(int i = 0; i < 10; i++) {
            for(int j = 0; j < 10; j++) {
                minHeight = Math.min(minHeight, area[i][j]);
            }
        }
        return minHeight;
    }

    /**
     * 2차원 배열 area중 가장 큰 값. 즉, 최고고도를 찾는 method입니다. 
     * 
     * @return area중 가장 큰 값
     */
    public double getMaxHeight () {
        double maxHeight = INF * -1;
        for(int i = 0; i < 10; i++) {
            for(int j = 0; j < 10; j++) {
                maxHeight = Math.max(maxHeight, area[i][j]);
            }
        }
        return maxHeight;
    }

    /**
     * area의 홍수 여부를 판단해 출력해주는 method입니다.
     * 해당 index에서의 값이 waterLevel보다 작을 경우 그 index에서의 고도가 물의 수위보다 낮음을 의미하고 *로 표시합니다.
     * 
     * @param waterLevel 홍수의 기준이 될 물의 수위
     */
    public void printFloodMap(double waterLevel) {
        System.out.println("Water Level: " + waterLevel);
        for(int i = 0; i < 10; i++) {
            for(int j = 0; j < 10; j++) {
                if(area[i][j] < waterLevel) {
                    System.out.print("* ");
                }
                else {
                    System.out.print("  ");
                }
            }
            System.out.println("");
        }
        System.out.println("");
    }
}