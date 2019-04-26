import java.util.Scanner;
public class fatema2
{
  public static void main(String args[])
  {
    Scanner input = new Scanner(System.in);
    int numCases = Integer.parseInt(input.nextLine());
    int count = 0;
    int sum = 0;
    for(int i = 0; i < numCases; i++)
    {
      String inputNums = input.nextLine();
      String[] nums = inputNums.split(" ");
      sum = 0;
      for(int j = 0; j < nums.length; j++)
      {
        sum = sum + Integer.parseInt(nums[j]);
      }
      count++;
      System.out.println("Case #" + count + ": " + Integer.toString(sum));
    }
  }
}