public class Average {
    public static double avg(int[] arr){
      int sum = 0;
      for (int val : arr)
      sum += val;
      return sum / arr.length;
  }
}
