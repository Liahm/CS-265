public class prob2
{
    public static void main(String[] args)
    {
        String s = args[0];
        int x = Integer.parseInt(s);
        if(x % 2 == 0)
        {
            System.out.println("Even");
        }
        else
            System.out.println("Odd");
    }
}