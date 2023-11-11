
import com.sun.source.tree.CatchTree;
import  java.util.*;

import java.util.Scanner;
public class School {
    public static void main(String[] args) {
        Scanner store = new Scanner(System.in);

        String lesson;
        String former;
        String edu= "Science";
        String pro1 = "Software";
        String course;
        String Relationship;
        String apply = "online";
        String iPassword;
        String verify;
        int contact;
        String cert;
        String shs = "WASSCE";
        String cbt = "CBT";
        String bond = "Acheampong";
        String Guardian;
        String entry;
        String module;
        String voucher;
        String iName;
        String tut = "Bright";
        String fName;
        String date1;
        String ref = "UYS2022";
        String payslip;
        String submit;
        int slip = 4739;
        int SSNIT;

        System.out.println("Welcome to UniYAT admission portal, choose applicant type");
        apply = store.nextLine();
        if (apply.equals("online")) {
            System.out.println("Corrections can be made after submission");
        } else if (apply.equals("offline")) {
            System.out.println("We do offer offline application here!");
        }

        System.out.println("Applicant Full Name");
        fName = store.nextLine();
        System.out.println("Enter applicant voucher");
        voucher = store.nextLine();
        while (voucher.isBlank()) {
            System.out.println("Buy vouchers at any CBG branch Nationwide");
            voucher = store.nextLine();
        }
        System.out.println("Choose course module");
        System.out.println("COMPETENT BASED TRAINING (CBT)");
        System.out.println("PROFESSIONAL");
        module = store.nextLine();
        store.nextLine();
        System.out.println("Enter Former School");
        former = store.nextLine();
        System.out.println("Former course");
        course = store.nextLine();
        System.out.println("Enter Your Current Certification");
        cert = store.nextLine();
        if (cert.equals(cbt)) {
            System.out.println(" Attach your CBT certificate  ");
        } else if (cert.equals(shs)) {
            System.out.println(" Attach your WASSCE certificate ");
        }
        System.out.println("The Administration will analyse your " + cert + " results !");

        System.out.println("Verify Application ID Number");
        verify = store.nextLine();
        if (verify.length() < 5) {
            System.out.println(" Incorrect ID number");
            store.nextLine();
        }

        System.out.println(" Name of Guardian");
        Guardian = store.nextLine();
        System.out.println("Applicant Relationship with Guardian");
        Relationship = store.nextLine();
        System.out.println("Choose Your Program");
        entry = store.nextLine();
        if (entry.equals(pro1) && course!=edu) {
            System.out.println(pro1 + " is reserved for Science students");
             store.nextLine();

        }
        System.out.println("Enter contact number");
        contact = store.nextInt();
        store.nextLine();
        System.out.println("Press Z to submit your Application");
        submit = store.nextLine();
        if (submit.equals("z") || submit.equals("Z")) {
            System.out.println(" Application successfully submitted ");

        }
        System.out.println(fName + " has applied for " + entry + " course " + " with the help of " + Guardian);
        System.out.println(" with approved " + cert + " from " + former);


        // instructor module

        System.out.println("Name of Instructor");
        iName = store.nextLine();

        if (iName.compareTo(tut) > 0) {
            System.out.println("Trying to log into someone account");
            store.nextLine();
        }
        System.out.println("Program Name");
        lesson = store.nextLine();

        if (lesson.compareTo(pro1) > 0) {
            System.out.println(" Program Name Does not correspond with instructor name");
            System.out.println("Enter Program Again!");
            store.nextLine();
        }
        System.out.println("SSNIT code to claim Your paycheck");
        SSNIT = store.nextInt();
        store.nextLine();
        if(SSNIT==slip) {
            System.out.println("Paycheck available for withdrawal");
        } else if (SSNIT != slip) {
            System.out.println("Payment of salary currently withold!");
            store.nextLine();
        }

        System.out.println("Enter Password");
        iPassword = store.nextLine();
        if (iPassword.isBlank()) {
            System.out.println("Password is compulsory");
        }
        System.out.println(iName + " of " + lesson + "logged into his account" + " using ref ID " + ref);
        store.close();

    }
   }

