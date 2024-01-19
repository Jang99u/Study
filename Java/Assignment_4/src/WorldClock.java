/**
 * WorldClock 클래스는 국제적 시간을 구해주는 클래스입니다.
 */
public class WorldClock extends Clock {
    private int setTime;

    /**
     * WorldClock 클래스의 기본 생성자입니다. WorldClock 객체를 초기화합니다.
     * 
     * @param setTime 현재 로컬지역의 시간과 국제적 시간의 차이
     */
    public WorldClock(int setTime) {
        this.setTime = setTime;
    }

    /**
     * Clock 클래스의 getHours method를 오버라이딩한 method입니다.
     * 현재 지역의 로컬타임의 시각을 구하고 setTime만큼 더해줍니다.
     * 
     * @return 국제시각
     */
    public int getHours() {
        int nowHours = Integer.parseInt(java.time.LocalTime.now().toString().substring(0, 2));
        nowHours += setTime;
        if(nowHours < 0) {
            nowHours = 24 + nowHours;
        }
        return nowHours;
    }
}
