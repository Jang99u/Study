public class BasicAccount extends BankAccount {
    public BasicAccount() {
        super();
    }
    
    public BasicAccount(double initialBalance) {
        super(initialBalance);
    }

    public void withdraw(double amount) {
        double panalty = 30;
        if(super.getBalance() >= amount) {
            super.withdraw(amount);
        } else {
            super.withdraw(amount + panalty);
        }
    }
}
