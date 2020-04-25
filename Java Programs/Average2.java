public class Average2 {
    public static void main(String[] args) {
      int[] arrr = {69, 420, 56, 92, 12};
      avg(arrr);
    }

    public static double avg(int[] arr) {
        int[] arrr = {69, 420, 56, 92, 12};
        double total = 0;

        for (int i = 0 ; i < arrr.length; i++){
          total = total + arrr[i];
        }

        double average = total / arrr.length;

        System.out.format("The average is: ");
        System.out.print(average);
        return average;
    }

}
