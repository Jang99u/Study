import java.util.Arrays;
import java.util.Random;

public class SortedSequence {
    public int[] generateRandom(int n) {
        Random generator = new Random();
        int arr[] = new int[n];

        for(int i = 0; i < n; i++) {
            int num = generator.nextInt(100);
            arr[i] = num;
        }

        return arr;
    }

    public void printArray(int[] values) {
        for(int i = 0; i < values.length; i++) {
            System.out.print(values[i] + " ");
        }
        System.out.print('\n');
    }

    public static void main(String[] args) {
        SortedSequence util = new SortedSequence();
        int[] values = util.generateRandom(20);
        
        util.printArray(values);
        Arrays.sort(values);
        util.printArray(values);
    }
}
