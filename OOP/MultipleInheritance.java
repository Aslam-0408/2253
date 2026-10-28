// First Interface
interface Printable {

    void print();
}

// Second Interface
interface Showable {

    void show();
}

// Class implementing multiple interfaces
class Student implements Printable, Showable {

    public void print() {
        System.out.println("Student is printing information.");
    }

    public void show() {
        System.out.println("Student is showing information.");
    }
}

// Main class
public class MultipleInheritance {

    public static void main(String[] args) {

        // Polymorphism using interface reference
        Printable p = new Student();
        Showable s = new Student();

        p.print();
        s.show();

        // Same object using both interfaces
        Student st = new Student();
        st.print();
        st.show();
    }
}