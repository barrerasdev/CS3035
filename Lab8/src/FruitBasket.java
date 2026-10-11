public class FruitBasket {
    private String fruitName;
    private String fruitColor;

    public FruitBasket(String fruitName, String fruitColor) {
        this.fruitName = fruitName;
        this.fruitColor = fruitColor;
    }

    public String whichFruit() {
        return "This fruit is a " + fruitColor + " colored " + fruitName + ".";
    }

    public boolean sameFruit(FruitBasket otherFruit) {
        return this.fruitName.equalsIgnoreCase(otherFruit.fruitName) &&
                this.fruitColor.equalsIgnoreCase(otherFruit.fruitColor);
    }

    public static void main(String[] args) {
        FruitBasket apple = new FruitBasket("Apple", "Red");
        FruitBasket banana = new FruitBasket("Banana", "Yellow");
        FruitBasket apple2 = new FruitBasket("apple", "red");

        System.out.println(apple.whichFruit());
        System.out.println("apple vs banana: " + apple.sameFruit(banana));
        System.out.println("apple vs apple2: " + apple.sameFruit(apple2));
    }
}
