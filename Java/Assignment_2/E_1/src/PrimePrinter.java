import java.util.Scanner;

/**
 * PrimeGenerator 클래스는 입력된 숫자까지의 모든 소수를 출력해주는 클래스입니다.
 */
public class PrimePrinter {
    /**
     * 사용자로부터 수를 입력받고 입력된 수까지의 모든 소수를 출력합니다.
     * PrimeGenerator 객체의 nextPrime 메서드의 반환값이 -1이라면 반복문을 탈출합니다.
     * 
     * @param args 생성할 소수의 제한범위를 외부로부터 받기 위한 문자열 인자
     */
    public static void main(String[] args) {
        Scanner keyIn = new Scanner(System.in);
        System.out.print("Enter how far you want to get prime numbers : ");
        int targetNum = keyIn.nextInt();
        PrimeGenerator primeGenerator = new PrimeGenerator(targetNum);

        int num = 1;
        while(true) {
            int nextNum = primeGenerator.nextPrime(num);
            if(nextNum == -1) break;
            System.out.print(nextNum + " ");
            num = nextNum + 1;
        }
        
        keyIn.close();
    }
}
