public class prob3
{
    public static void main(String[] args)
    {
        String s = args[0];
        int year = Integer.parseInt(s);

        if(year%4 == 0)
        {
            if(year%100 == 0)
            {
                if(year%400 == 0)
                System.out.println("Leap Year");
                else              
                System.out.println("Not a leap year!");
            }
            else
                System.out.println("Leap Year!");        
        }
        else
            System.out.println("Not a leap year!");
    }
}