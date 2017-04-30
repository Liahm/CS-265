import java.util.Date;

public class prob4
{
    public static void main(String[] args)
    {
        String s = args[0];
        int time = Integer.parseInt(s);
        Date today = new Date();
        long milliseconds = today.getTime();

        switch(time)
        {
            case 0:
                System.out.println("Milliseconds since January 1, 1970: " + milliseconds);
                break;
            case 1:
                System.out.println("seconds since January 1, 1970: " + milliseconds/1000);
                break;
            case 2:
                System.out.println("Days since January 1, 1970: " + (milliseconds/1000)/86400);
                break;
            case 3:
                System.out.println("Today is: " + today.toString());
                break;
        }
    }
}