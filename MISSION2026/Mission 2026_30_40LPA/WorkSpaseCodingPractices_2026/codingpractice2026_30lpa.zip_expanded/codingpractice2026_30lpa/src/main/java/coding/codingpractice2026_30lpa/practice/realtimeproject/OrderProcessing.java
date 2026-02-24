package coding.codingpractice2026_30lpa.practice.realtimeproject;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class EmailService implements Runnable {
    private String email;

    EmailService(String email) {
        this.email = email;
    }

    public void run() {
        System.out.println("Sending email to " + email + " by " + Thread.currentThread().getName());
    }
}

class InventoryService implements Runnable {
    private String product;

    InventoryService(String product) {
        this.product = product;
    }

    public void run() {
        System.out.println("Updating inventory for " + product + " by " + Thread.currentThread().getName());
    }
}

public class OrderProcessing {

    public static void main(String[] args) {

        ExecutorService executor = Executors.newFixedThreadPool(2);

        // Parallel background tasks
        executor.submit(new EmailService("customer@gmail.com"));
        executor.submit(new InventoryService("Laptop"));
System.out.println("hello java ");
        executor.shutdown();
    }
}
