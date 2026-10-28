import java.util.Scanner;

public class Calculator {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        boolean running = true;

        System.out.println("===== JAVA CALCULATOR =====");

        while (running) {

            try {
                System.out.println("\nSelect an Operation:");
                System.out.println("1. Addition (+)");
                System.out.println("2. Subtraction (-)");
                System.out.println("3. Multiplication (*)");
                System.out.println("4. Division (/)");
                System.out.println("5. Modulus (%)");
                System.out.println("6. Exit");

                System.out.print("Enter your choice: ");
                int choice = sc.nextInt();

                if (choice == 6) {
                    System.out.println("Calculator closed. Thank you!");
                    running = false;
                    continue;
                }

                if (choice < 1 || choice > 6) {
                    System.out.println("Invalid choice! Please select 1 to 6.");
                    continue;
                }

                System.out.print("Enter first number: ");
                double num1 = sc.nextDouble();

                System.out.print("Enter second number: ");
                double num2 = sc.nextDouble();

                double result;

                switch (choice) {

                    case 1:
                        result = num1 + num2;
                        System.out.println("Result = " + result);
                        break;

                    case 2:
                        result = num1 - num2;
                        System.out.println("Result = " + result);
                        break;

                    case 3:
                        result = num1 * num2;
                        System.out.println("Result = " + result);
                        break;

                    case 4:
                        if (num2 == 0) {
                            System.out.println("Error: Division by zero is not allowed.");
                        } else {
                            result = num1 / num2;
                            System.out.println("Result = " + result);
                        }
                        break;

                    case 5:
                        if (num2 == 0) {
                            System.out.println("Error: Modulus by zero is not allowed.");
                        } else {
                            result = num1 % num2;
                            System.out.println("Result = " + result);
                        }
                        break;
                }

            } catch (Exception e) {

                System.out.println("Invalid input! Please enter numbers only.");
                sc.nextLine(); // Clear invalid input
            }
        }

        sc.close();
    }
}