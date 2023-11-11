import java.util.Scanner;


public class App {
    public static void main(String[] args) throws Exception {
        String name;
        Scanner key = new Scanner(System.in);
        System.out.println("Enter name here");
        name = key.nextLine();
        if(name.equals("Rose")){
            System.out.println("Hi mom");
        }else if(name.contains(" ")){
         System.out.println("Name must not have symbol");
        }
        key.close();
    }
}
