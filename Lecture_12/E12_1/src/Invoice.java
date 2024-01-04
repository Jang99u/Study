import java.util.ArrayList;

public class Invoice {
   private Address billingAddress;
   private ArrayList<LineItem>items;
   
   public Invoice(Address anAddress)
   {
      items = new ArrayList<LineItem>();
      billingAddress = anAddress;
   }
   
   public void add(Product aProduct, int quantity)
   {
      LineItem anItem = new LineItem(aProduct, quantity);
      items.add(anItem);
   }
   
   public String format()
   {
      String r = String.format("%32s%n%n", "I N V O I C E")
            + billingAddress.format()
            + String.format("%n%n%-30s%8s%5s%8s%n", 
                  "Description","Price","Qty","Total");
      for(LineItem item : items)
      {
         r = String.format("%s%s%n",r,item.format());
      }
      r = r + String.format("%nAMOUNT DUE: $%8.2f%n",getAmountDue());
      return r;
   }
   private double getAmountDue()
   {
      double amountDue = 0;
      for(LineItem item : items)
      {
         amountDue = amountDue + item.getTotalPrice();
      }
      return amountDue;
   }

}