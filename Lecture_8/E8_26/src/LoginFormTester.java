public class LoginFormTester {
    public static void main(String[] args) {
        LoginForm login = new LoginForm("admin", "admin123");

        login.input("test");
        login.input("test123");
        login.click("Submit");

        login.click("Reset");
        login.input("admin");
        login.input("admin123");
        login.click("Submit");
    }
}
