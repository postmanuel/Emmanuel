
import java.util.ArrayList;

public class index {

        public static void main(String[] args) {
            //ArrayList object
            ArrayList arrList = new ArrayList();

            //adding elements in the list
            arrList.add("100");
            arrList.add("200");
            arrList.add("123");
            arrList.add("234");
            arrList.add("11");
            arrList.add("300");
            arrList.add("400");
            arrList.add("500");

            //searching element "300"
            int ind = arrList.indexOf("400");
                System.out.println("Element found @ index: " + ind);
        }

    }

