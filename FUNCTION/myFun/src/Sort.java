
    import java.util.Scanner;

    public class Sort {
        static Scanner in;
        public static void main(String[] args) {
            int i, j, n;
            in = new Scanner(System.in);
            System.out.print("Enter the value of n \n");
            n = in .nextInt();
            String[] name = new String[8];
            String[] tname = new String[8];
            String temp;

            System.out.println("Enter " + n + " names");
            in .nextLine();
            for (i = 0; i < n; i++) {
                name[i] = in .nextLine();
                tname[i] = name[i];
            }
            for (i = 0; i < n - 1; i++) {
                for (j = i + 1; j < n; j++) {
                    if (name[i].compareToIgnoreCase(name[j]) > 0) {
                        temp = name[i];
                        name[i] = name[j];
                        name[j] = temp;
                    }
                }
            }


            for (i = 0; i < n; i++) {
                System.out.printf(tname[i] + "\t\t\t" + name[i] + "\n");
            }

        }
    }

