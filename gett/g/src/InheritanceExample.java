public class InheritanceExample {
    public static void main(String[] args) {
        
        Animal genericAnimal = new Animal(" Wolf " ,"black");
        Dog myDog = new Dog("Buddy"," black");
        genericAnimal.fetch();
        genericAnimal.eat();
        genericAnimal.speak(); // Output: Generic Animal makes a soun
        myDog.speak();         // Output: Buddy barks.
        myDog.fetch();// Output: Buddy fetches a ball.
        myDog.eat();
    }
}
