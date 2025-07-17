import java.util.Scanner;

public class Palindrome {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter String: ");

    String s = sc.nextLine();
    String rev = "";
    for(int i=0; i<s.length(); i++) {
      rev = s.charAt(i) + rev;
    }
    if(s.equalsIgnoreCase(rev)) {
      System.out.println(s + " is a Palindrome");
    }
    else {
      System.out.println(s + " is not a Palindrome");
    }
  }
}
