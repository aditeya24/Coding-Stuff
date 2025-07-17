import java.util.Scanner;

public class StringWhitespaceRemove {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter String: ");
        String s = sc.nextLine();

        String s_no_ws = "";

        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) != ' ') {
                s_no_ws = s_no_ws + s.charAt(i);
            }
        }

        System.out.println(s_no_ws);
    }
}
