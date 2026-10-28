class ChatUser extends Thread {

    private String userName;
    private volatile boolean running = true;
    private volatile boolean suspended = false;

    public ChatUser(String userName) {
        this.userName = userName;
    }

    public void sendMessage(String message) {
        System.out.println(userName + " sends: " + message);
    }

    public void receiveMessage(String message) {
        System.out.println(userName + " receives: " + message);
    }

    public void suspendThread() {
        suspended = true;
        System.out.println(userName + " is suspended.");
    }

    public void resumeThread() {
        suspended = false;
        System.out.println(userName + " is resumed.");
    }

    public void stopThread() {
        running = false;
        System.out.println(userName + " is stopped.");
    }

    @Override
    public void run() {

        int count = 1;

        while (running && count <= 5) {

            while (suspended && running) {
                try {
                    Thread.sleep(200);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }

            if (!running) {
                break;
            }

            System.out.println(userName + " is active - Message " + count);

            count++;

            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }

        System.out.println(userName + " thread has finished.");
    }
}


public class ChatApplication {

    public static void main(String[] args) {

        ChatUser user1 = new ChatUser("Alice");
        ChatUser user2 = new ChatUser("Bob");

        user1.setPriority(Thread.MAX_PRIORITY);
        user2.setPriority(Thread.NORM_PRIORITY);

        System.out.println("===== BASIC CHAT SYSTEM =====");

        user1.start();
        user2.start();

        System.out.println("\nThread Status:");
        System.out.println("Alice is alive: " + user1.isAlive());
        System.out.println("Bob is alive: " + user2.isAlive());

        user1.sendMessage("Hello Bob!");
        user2.receiveMessage("Hello Bob!");

        user2.sendMessage("Hi Alice!");
        user1.receiveMessage("Hi Alice!");

        try {
            Thread.sleep(800);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        user2.suspendThread();

        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        user2.resumeThread();

        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        user1.stopThread();

        try {
            user1.join();
            user2.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println("\nFinal Thread Status:");
        System.out.println("Alice is alive: " + user1.isAlive());
        System.out.println("Bob is alive: " + user2.isAlive());

        System.out.println("\nChat application finished.");
    }
}