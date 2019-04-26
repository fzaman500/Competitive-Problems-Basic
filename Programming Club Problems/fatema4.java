import java.util.Scanner;
public class fatema4
{
  public static void main(String args[])
  {
    Scanner input = new Scanner(System.in);
    int numDays = Integer.parseInt(input.nextLine());
    int count = 1;
    int total = 0;
    for(int i = 0; i < numDays; i++)
    {
      String inputNums = input.nextLine();
      String[] nums = inputNums.split(" ");
      total = total + Integer.parseInt(nums[0]) - Integer.parseInt(nums[1]);
      System.out.println("Day #" + count + ": Total profit is " + Integer.toString(total));
      count++;
    }
  }
}