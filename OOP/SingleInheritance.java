// Superclass
class Animal {

    void eat() {
        System.out.println("Animal is eating.");
    }

    void sleep() {
        System.out.println("Animal is sleeping.");
    }
}

// Subclass
class Dog extends Animal {

    void bark() {
        System.out.println("Dog is barking.");
    }
}

// Main class
public class SingleInheritance {

    public static void main(String[] args) {

        Dog d = new Dog();

        // Calling superclass methods
        d.eat();
        d.sleep();

        // Calling subclass method
        d.bark();
    }
}