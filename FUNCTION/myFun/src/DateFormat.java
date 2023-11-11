//import java.text.SimpleDateFormat;
//import java.util.*;
//public class DateFormat {
//
////    public class ConvDateString2DatePrg {
//        public static void main(String [] args) {
//            try {
//                //define date format to take input
//                SimpleDateFormat dateF = new SimpleDateFormat("dd/MM/yyyy");
//
//                Scanner sc = new Scanner(System.in); //string object
//                String dtString = "";
//
//                System.out.print("Enter date in dd/MM/yyyy format:");
//                dtString = sc.nextLine();
//
//                //convert input date string into Date
//                Date dt = dateF.parse(dtString);
//
//                System.out.print("Entered Date is: " + dt.toString());
//            } catch (Exception exception) {
//                System.out.println("Exception is: " + exception.toString());
//            }
//        }
//
//}
//package to class Date class


import java.util.Date;

public class DateFormat {
    public static void main(String args[]) {
        //creating object of Date class
        Date dt = new Date();
        //printing the date and time
        System.out.print("Current system date and time is: "+ dt.toString());
    }
}
