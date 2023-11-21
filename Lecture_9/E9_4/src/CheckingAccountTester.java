public class CheckingAccountTester {
    public static void main(String[] args) {
        BankAccount account = new CheckingAccount();
        account.deposit(100.00);
        System.out.println(account.getBalance());

        account.withdraw(90.00);
        System.out.println(account.getBalance());

        account.withdraw(20.00);
        System.out.println(account.getBalance());

        account.withdraw(20.00);
        System.out.println(account.getBalance());

        account.withdraw(20.00);
        System.out.println(account.getBalance());

        account.monthEnd();
        account.deposit(151);
        System.out.println(account.getBalance());

        account.withdraw(20.00);
        System.out.println(account.getBalance());
    }
}
