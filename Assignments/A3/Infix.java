//Name: Eric Lee
//Java version: JDK-8u111 8.0_111
//It's a calculator that takes infix (Normal math) into postfix(Numbers first, then sign) and =

import java.util.*;
import java.io.*;
//import java.util.Stack; //To use stack, could had also use List

//Copied from Operand.java from ~Kschmidt/.../Java-Calc/Token.java
abstract class Token{

    abstract boolean isOperator();
    abstract boolean isOperand();
}

//Copied from Operand.java from ~Kschmidt/.../Java-Calc/Operand.java
public class Operand extends Token 
{
    protected int val;

    public boolean isOperator() 
    {
        return false;
    }
    public boolean isOperand()
    {
        return true;
    }
    public int getVal()
    {
        return val;
    }
    public Operand(int v)
    {
        val = v;
    }

}

//Copied from Operand.java from ~Kschmidt/.../Java-Calc/Operator.java
public class Operator extends Token
{
    protected opType val;

    public boolean isOperator()
    {
        return true;
    }
    public boolean isOperand()
    {
        return false;
    }

    protected int getPrec()
    {
        //TODO: use a switch, whatever, assign ordinals to operators
        //I am sure I don't need that many
        if(val.equals("()") || val.equals("[]") || val.equals("->") || val.equals(".") || val.equals("::"))
            return 1;
        else if(val.equals("*") || val.equals("/") || val.equals("%"))
            return 3;
        else if(val.equals("+") || val.equals("-"))
            return 4;
        else if(val.equals("<<") || val.equals(">>"))
            return 5;    
        else if(val.equals("<") || val.equals("<=") || val.equals(">") || val.equals(">="))
            return 6;
        else if(val.equals("==") || val.equals("!="))
            return 7;
        else if(val.equals("&"))
            return 8;
        else if(val.equals("^"))
            return 10;     
        else if(val.equals("|"))
            return 10;    
        else if(val.equals("&&"))
            return 11;
        else if(val.equals("||"))
            return 12;

        return 0;
    }

        //handy for comparing 2 operators
    public static int compare(Operator a, Operator b)
    {
        if( a.getPrec() == b.getPrec())
            return 0;
        else if( a.getPrec() < b.getPrec())
            return -1;
        else
            return 1; 
    }

    public opType getVal()
    {
        return val;
    }
    public Operator( opType v)
    {
        val = v;
    }
}

//Copied from Operand.java from ~Kschmidt/.../Java-Calc/opType.java
public final class opType
{
    public static opType ADD = new opType ("ADD");
    public static opType SUB = new opType ("SUB");
    public static opType MULT = new opType ("MULT");
    public static opType DIV = new opType ("DIV");
    public static opType MOD = new opType ("MOD");
    public static opType LPAR = new opType ("LPAR");
    public static opType RPAR = new opType ("RPAR");

    protected String name;

    private opType( String n)
    {
        name = n;
    }

    public String getName() // for debugging, maybe
    {
        return name;
    }

    public static void main( String argv[]) //testing
    {
        opType a = opType.ADD;
        opType b = opType.ADD;
        opType c = opType.MULT;
        
        if(a != b)
            System.out.println( "a and b should be the same (ADD)");

        if( a == c )
            System.out.println( " a and c should not be the same (ADD vs. Mult)");
            
        if( b == c )
            System.out.println( " a and c should not be the same (ADD vs. Mult)");

        System.out.println("Done!");
    }
}

public class infix{

    void infix2postfix (String infix[], String post[]) //Method that will change the input into a postfix.
    {
        Stack<String> stack = new Stack<String>();
        while (!StdIn.isEmpty()) {
            String s = StdIn.readString();
            if      (s.equals("+")) 
                stack.push(s);
            else if (s.equals("-")) 
                stack.push(s);
            else if (s.equals("*")) 
                stack.push(s);
            else if (s.equals("/")) 
                stack.push(s);
            else if (s.equals("%")) 
                stack.push(s);
            else if (s.equals(")")) 
                StdOut.print(stack.pop() + " ");
            else if (s.equals("(")) 
                StdOut.print("");
            else                    
                StdOut.print(s + " ");
        }
        StdOut.println();

    }

    public static void evalPostfix (String[] args)
    {
        Stack<String> ops  = new Stack<String>();
        Stack<Double> vals = new Stack<Double>();

        while (!StdIn.isEmpty()) {
            String s = StdIn.readString();
            if(s.equals("("));
            else if (s.equals("+"))
            	ops.push(s);
            else if (s.equals("-"))
            	ops.push(s);
            else if (s.equals("*"))
            	ops.push(s);
            else if (s.equals("/")) 
            	ops.push(s);
            else if (s.equals(")"))
            {
                String op = ops.pop();
                double v = vals.pop();
                if      (op.equals("+")) 
                	v = vals.pop() + v;
                else if (op.equals("-")) 
                	v = vals.pop() - v;
                else if (op.equals("*"))  
                	v = vals.pop() * v;
                else if (op.equals("/"))  
                	v = vals.pop() / v;
                else if (op.equals("sqrt"))
                	v = Math.sqrt(v);
                vals.push(v);
            }
            else vals.push(Double.parseDouble(s));
        }
        StdOut.println(vals.pop());
    }
    }

}


class calculator //"Where the magic occurs", literally here is where I show the result
{
    public static void main(String result) //This is the main function
    {
        //change it to read equations from a file.
        //Each equation is \n of difference
        System.out.println("Apply Infix here for calculation");
        String input = System.console().readLine();
        System.out.println(input, " = ", evalPostfix(infix2postfix(result)), "=");
    }

}


		
		Stack<Character> operators = new Stack<Character>();
		List<Object> postfix = new LinkedList<Object>();

		int stack = 0;
		boolean stackOperand = false;
		for(char c : s.toCharArray())
    	{
    		if(c>= '0' && c <= '9')
    		{
    			stack = stack * 10 + c - '0';
    			stackOperand = true;
    		}
    		else
    		{
    			if(stackOperand)
    				postfix.add(stack);
    			stack = 0;
    			stackOperand = false;
    			
    			if(c == ' ' || c == '\t') //If given a space or tab, ignore it
    				continue;
    			if(c == '(') //Push (
    				operators.push('(');
    			else if(c == ')')
    			{
    				while (operators.peek() != '(')
    					postfix.add(operators.pop());
    				operators.pop(); //This will move the '(' to close ')'
    			}
    			else
    			{//I moves the operator
    				while(!operators.isEmpty() && Operator.getPrec() <= Operator.getPrec(operators.peek()))
    					postfix.add(operators.pop());
    				operators.push(c);