import java.util.Scanner;

class BinarySearch{
  public static void main(String[] args) {
    Scanner obj = new Scanner(System.in);
    System.out.println("Enter the search term: ");
    int x = obj.nextInt(); 
    String y = binarySearch(x);
    System.out.println("The search term was " + y);
  }
  static String binarySearch(int x) {
    int[] array = {1,2,3,4,5};
    int start = 0, end = array.length - 1 ; 
    while (start <= end) {
      int middle = (start + end) / 2;
      if(x == array[middle])
        return "found at index " + String.valueOf(middle);
      else if(x > array[middle])
        start = middle + 1;
      else if(x < array[middle])
        end = middle - 1;
    }
    return "not found";
  }
}

