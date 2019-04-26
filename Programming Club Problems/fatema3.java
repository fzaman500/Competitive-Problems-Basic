import java.util.Scanner;
public class fatema3
{
  public static void main(String args[])
  {
    Scanner input = new Scanner(System.in);
    int numCases = Integer.parseInt(input.nextLine());
    int count = 1;
    for(int i = 0; i < numCases; i++)
    {
      String word = "";
      int numWords = Integer.parseInt(input.nextLine());
      for(int j = 0; j < numWords; j++)
      {
        word = word + " " + input.nextLine();
      }
      System.out.print("Case #" + count + ":" + word);
      System.out.println();
      count++;
    }
  }
}