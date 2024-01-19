public class BasicAccountTester {
    public static void main(String[] args) {
        BankAccount account = new BasicAccount(100.00);

        account.withdraw(80.00);
        System.out.println(account.getBalance());
        
        account.withdraw(50.00);
        System.out.println(account.getBalance());

        account.withdraw(50.00);
        System.out.println(account.getBalance());
    }
}
