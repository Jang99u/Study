/**
 * Clock 클래스는 현재 지역의 시간을 구해주는 클래스입니다.
 */
public class Clock {
    /**
     * 현재 지역의 로컬타임의 시각을 구해주는 method 입니다.
     * 
     * @return 현재 지역의 시
     */
    public int getHours() {
        int nowHours = Integer.parseInt(java.time.LocalTime.now().toString().substring(0, 2));
        return nowHours;
    }

    /**
     * 현재 지역의 로컬타임의 분을 구해주는 method입니다.
     * 
     * @return 현재 지역의 분
     */
    public int getMinutes() {
        int nowMinutes = Integer.parseInt(java.time.LocalTime.now().toString().substring(3, 5));;
        return nowMinutes;
    }

    /**
     * 현재 지역의 시각과 분을 구해주는 method입니다.
     * 
     * @return 현재 지역의 시와 분을 String 형태로 반환
     */
    public String getTime() {
        return getHours() + ":" + getMinutes();
    }
}