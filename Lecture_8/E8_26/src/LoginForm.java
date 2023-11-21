public class LoginForm {
    private String username;
    private String password;
    private String currentUsername;
    private String currentPassword;
    private boolean logged;
    private boolean firstInput;

    public LoginForm(String n, String p) {
        username = n;
        password = p;
        firstInput = true;
    }

    private boolean checkLogin() {
        if(currentUsername.equals(username) && currentPassword.equals(password)) return true;
        else {
            reset();
            return false;
        }
    }
    
    private void reset() {
        firstInput = true;
    }

    public void input(String text) {
        if(firstInput) {
            currentUsername = new String(text);
            firstInput = false;
        }
        else {
            currentPassword = new String(text);
        }
    }

    public void click(String button) {
        if (button.equals("Submit")) {
            if (checkLogin()) {
                this.logged = true;
                System.out.println("User is logged in.");
            }
            else {
                System.out.println("User in not logged in.");
            }
        }
        else if (button.equals("Reset")) {
            reset();
        }
    }

    public boolean loggedIn() {
        if(logged) return true;
        else return false;
    }
}