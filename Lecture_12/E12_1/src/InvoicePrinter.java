import java.util.Scanner;

public class InvoicePrinter {
   public static void main(String[] args)
   {
      Scanner in = new Scanner(System.in);
      System.out.println("Thos program reads an invoice(name, address, products purchased) and prints an invoice.");
      
      System.out.print("Please enter an address (empty line to terminate)\nName: ");
      String name = in.nextLine();
      System.out.print("Street: ");
      String street = in.nextLine();
      System.out.print("City: ");
      String city = in.nextLine();
      System.out.print("State: ");
      String state = in.nextLine();
      System.out.print("Zipcode: ");
      String zipcode = in.nextLine();
      
      Address address = new Address(name, street, city, state, zipcode);
      Invoice invoice = new Invoice(address);
      while (true)
      {
        System.out.print("Product description (empty line to terminate):\n");
        String productName = in.nextLine();
        if(productName.equals("")) break;
        System.out.print("Price: ");
        double price = in.nextDouble();
        System.out.print("Quantity: ");
        int quantity = in.nextInt();
        in.nextLine();
         
        invoice.add(new Product(productName, price), quantity);
      }
      
      System.out.println(invoice.format());

      in.close();
   }
}