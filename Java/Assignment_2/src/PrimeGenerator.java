/**
 * PrimeGenerator 클래스는 소수를 만들어주는 클래스입니다.
 */
public class PrimeGenerator {
    private int limitNum;

    /**
     * PrimeGenerator 클래스의 기본 생성자입니다. PrimeGenerator 객체를 초기화합니다.
     * 
     * @param inputNum 생성할 소수의 제한범위
     */
    public PrimeGenerator(int inputNum) {
        limitNum = inputNum;
    }

    /**
     * parameter로 입력된 수보다 크거나 같은 소수 중 가장 작은 nextNum을 구하는 method입니다.
     * 만약 nextNum이 limitNum을 넘어선다면 -1을 반환해 제한 범위를 넘어섰다는 것을 알려줍니다.
     * 
     * @param num num 검색을 시작할 숫자
     * @return 입력된 수보다 크거나 같은 소수 중 가장 작은 수
     */
    public int nextPrime(int num) {
        int nextNum;
        for(nextNum = num; ; nextNum++) {
            if(isPrime(nextNum)) break;
        }
        if(nextNum > limitNum) return -1;
        return nextNum;
    }

    /**
     * 주어진 숫자 num이 소수인지 판별하는 method입니다.
     * 
     * @param num 소수 여부를 판별할 숫자
     * @return 주어진 숫자가 소수면 true를, 그렇지 않다면 false를 반환
     */
    public boolean isPrime(int num) {
        if(num == 1) return false;
        for(int i = 2; i < num-1; i++) {
            if(num % i == 0) return false;
        }
        return true;
    }
}
