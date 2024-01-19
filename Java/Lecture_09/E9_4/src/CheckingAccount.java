public class CheckingAccount extends BankAccount {
    private boolean firstWithdraw = true;
    
    public CheckingAccount() {
        super();
    }

    public CheckingAccount(double initialBalance) {
        super(initialBalance);
    }

    public void withdraw(double amount) {
        if(super.getBalance() >= amount) {
            super.withdraw(amount);
        } else {
            if(firstWithdraw) {
                super.withdraw(amount+20);
                firstWithdraw = false;
            } else {
                super.withdraw(amount+30);
            }
        }
    }
}
