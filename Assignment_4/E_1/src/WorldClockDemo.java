/**
 * WorldClockDemo 클래스는 WorldClock 클래스가 정상적으로 작동하는지 보기 위한 클래스입니다.
 */
public class WorldClockDemo {
    /**
     * 국제시각과의 시차를 offset 변수에 저장합니다.
     * Clock 객체와 WorldClock 객체를 생성해주고 method를 테스트합니다.
     * 
     * @param args
     */
    public static void main(String[] args) {
        int offset = -14;
        Clock clock = new Clock();
        Clock worldClock = new WorldClock(offset);

        System.out.println("Base Time in Current Time-Zone");
        System.out.println("Hours: " + clock.getHours());
        System.out.println("Minutes: " + clock.getMinutes());
        System.out.println("Time: " + clock.getTime());

        System.out.println("World Clock Offset: " + offset);
        System.out.println("Hours: " + worldClock.getHours());
        System.out.println("Minutes: " + worldClock.getMinutes());
        System.out.println("Time: " + worldClock.getTime());
    }
}
