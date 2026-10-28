import java.util.Scanner;

class ATM {

    private double balance;

    // Constructor
    ATM(double initialBalance) {
        if (initialBalance < 0) {
            throw new IllegalArgumentException("Initial balance cannot be negative.");
        }
        balance = initialBalance;
    }

    // Check balance
    void checkBalance() {
        System.out.println("Current Balance: Rs. " + balance);
    }

    // Deposit money
    void deposit(double amount) {

        if (amount <= 0) {
            throw new IllegalArgumentException(
                "Deposit amount must be greater than zero."
            );
        }

        balance = balance + amount;
        System.out.println("Rs. " + amount + " deposited successfully.");
    }

    // Withdraw money
    void withdraw(double amount) {

        if (amount <= 0) {
            throw new IllegalArgumentException(
                "Withdrawal amount must be greater than zero."
            );
        }

        if (amount > balance) {
            throw new ArithmeticException(
                "Insufficient funds! Available balance: Rs. " + balance
            );
        }

        balance = balance - amount;
        System.out.println("Rs. " + amount + " withdrawn successfully.");
    }
}

public class ATMSimulation {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        ATM atm = new ATM(10000);
        boolean running = true;

        System.out.println("===== ATM MACHINE =====");

        while (running) {

            try {

                System.out.println("\n1. Check Balance");
                System.out.println("2. Deposit Money");
                System.out.println("3. Withdraw Money");
                System.out.println("4. Exit");

                System.out.print("Enter your choice: ");
                int choice = sc.nextInt();

                switch (choice) {

                    case 1:
                        atm.checkBalance();
                        break;

                    case 2:
                        System.out.print("Enter deposit amount: ");
                        double depositAmount = sc.nextDouble();
                        atm.deposit(depositAmount);
                        break;

                    case 3:
                        System.out.print("Enter withdrawal amount: ");
                        double withdrawAmount = sc.nextDouble();
                        atm.withdraw(withdrawAmount);
                        break;

                    case 4:
                        System.out.println("Thank you for using the ATM.");
                        running = false;
                        break;

                    default:
                        throw new IllegalArgumentException(
                            "Invalid choice! Please select 1 to 4."
                        );
                }

            } catch (ArithmeticException e) {

                System.out.println("Error: " + e.getMessage());

            } catch (IllegalArgumentException e) {

                System.out.println("Invalid Input: " + e.getMessage());

            } catch (Exception e) {

                System.out.println("Please enter valid numeric input.");
                sc.nextLine();

            } finally {

                System.out.println("Transaction process completed.");

            }
        }

        sc.close();
    }
}