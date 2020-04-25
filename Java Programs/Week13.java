public class Week13 {
  public static void main (String[] args) {
    System.out.print("Hello World");

    int[] ar = new int[10];
    for(int i = 0; i < 10; i++){
      for (int j = 0; j < 10; i++){
        System.out.println("Hi");
        //ar[i] = i+j;
      }
    }
    System.out.println("Array created...");

    for (int i = 0; i < ar.length; i++) {
      System.out.println(ar[i]);
    }
  }
}
