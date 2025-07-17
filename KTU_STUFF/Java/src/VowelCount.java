import java.util.Scanner;

public class VowelCount {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter String: ");
        String s = sc.nextLine();

        int v_count = 0, c_count = 0;

        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) == 'a' || s.charAt(i) == 'e' || s.charAt(i) == 'i' || s.charAt(i) == 'o' || s.charAt(i) == 'u')
                v_count++;
            else
                c_count++;
        }

        System.out.println("Vowels: "+v_count+"\nConsonants: "+c_count);
    }
}
