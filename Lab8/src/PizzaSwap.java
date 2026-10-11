public class PizzaSwap {

    static class PizzaOrder {
        int count;

        PizzaOrder(int count) {
            this.count = count;
        }
    }

    public static void swap(PizzaOrder a, PizzaOrder b) {
        int temp = a.count;
        a.count = b.count;
        b.count = temp;
    }

    public static void main(String[] args) {
        PizzaOrder customer1 = new PizzaOrder(9);
        PizzaOrder customer2 = new PizzaOrder(4);

        System.out.println("Before swap:");
        System.out.println("Customer 1 pizzas: " + customer1.count);
        System.out.println("Customer 2 pizzas: " + customer2.count);

        swap(customer1, customer2);

        System.out.println("\nAfter swap:");
        System.out.println("Customer 1 pizzas: " + customer1.count);
        System.out.println("Customer 2 pizzas: " + customer2.count);
    }
}