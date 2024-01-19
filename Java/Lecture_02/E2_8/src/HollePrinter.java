public class HollePrinter {
    public static void main(String[] args) {
        String str = "Hello, World!";

        for(int i = 0; i < str.length(); i++)
        {
            if(str.charAt(i) == 'e') System.out.print('o');
            else if(str.charAt(i) == 'o') System.out.print('e');
            else System.out.print(str.charAt(i));
        }
    }
}