public class Recurse {
    public static void main(String[] args) {
        int result = sum(15, 13);
        System.out.println(result);
    }
    public static int sum(int start, int end) {
        if (end > start) {
            return end + sum(start, end + 2);
        } else {
            return end;
        }
    }
    }

