public class Address {
   private String name;
   private String street;
   private String city;
   private String state;
   private String zip;
   
   public Address(String aName, String aStreet, String aCity, String aState, String aZip) {
      name = aName;
      street = aStreet;
      city = aCity;
      state = aState;
      zip = aZip;
   }
   
   public String format() {
      return String.format("%s%n%s%n%s, %s %s", name, street, city, state, zip);
   }
}