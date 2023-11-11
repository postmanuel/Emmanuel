public class Taurus extends Wolf{
    public Taurus(String name, double weight, int age) {
        super(name, weight, age);



    }
    public void speak() {
        System.out.println("I am a Taurus guy " + this.name + " is my name " + this.age + " is my age"
            + " and i weigh "  + this.weight);
    }
}
