import java.util.List;
import java.util.ArrayList;

public class Bag {
    private static class Item {
        private String name;
        private int quantity;

        public Item(String name) {
            this.name = name;
            this.quantity = 1;
        }
    }

    private List<Item> items;

    public Bag() {
        items = new ArrayList<Item>();
    }

    public void add(String item) {
        for(Item product : items) {
            if(product.name == item) {
                product.quantity += 1;
                return;
            }
        }
        Item input = new Item(item);
        items.add(input);
    }

    public int count(String item) {
        for(Item product : items) {
            if(product.name == item) {
                return product.quantity;
            }
        }
        return 0;
    }
}