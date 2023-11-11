import java.awt.*;


// Parent class (or superclass)
class Animal {
    String name;
    String colour ;
    Animal(String name, String colour) {
        this.name = name;
        this.colour =colour;
    }

    void fetch() {

        System.out.println(name + " fetches a ball.");
        System.out.println(name + "  has a " + colour + " colour");
    }
    void eat(){
        System.out.println(name + " eat good food daily");
    }
    void speak() {
        System.out.println(name + " makes a sound.");
    }
}

// Child class (or subclass) that inherits from Animal
class Dog extends Animal {
    Dog(String name, String colour) {
        super(name, colour); // Call the constructor of the superclass
    }
    @Override
    void speak() {
        System.out.println(name + " barks.");
        //System.out.println(name + " has colour " + colour);
    }
    void fetch() {
        System.out.println(name + " fetches a ball.");
    }
}

