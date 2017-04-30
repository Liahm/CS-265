/*@Name: Eric Lee
 *@Java version: JDK-8u111 8.0_111
 *@It's a calculator that takes infix (Normal math) into postfix(Numbers first, then sign) and =
 *
 * Assumptions:
 * 	Arimethic expression has only integer operands
 * Only +, -, *, / and % operators are allowed
 * Usual rules of precedence are asuumed
 * Parentheses are allowed
 */
package Infix2Postfix;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;
import java.io.*;
//import java.util.StringTokenizer;

public class infix2Postfix
{

	static List<Object> infix2Postfix(String exp)
	{
		//Other option was to use tokenizer.
		Stack<Character> operators = new Stack<Character>(); 
		List<Object> postfix = new LinkedList<Object>();
		
		int stack = 0;
		boolean stackOperand = false;
		
		for(char c : exp.toCharArray()) //loop of c through the array
		{
			if(c>= '0' && c <= '9') //If c is a number, then update stack and boolean
			{
				stack = stack * 10 + c - '0';
				stackOperand = true;
			}
			else
			{
				if(stackOperand)
					postfix.add(stack); //add to the stack
				stack = 0;
				stackOperand = false;
			
				if(c == ' ' || c == '\t') //If given a space or tab, ignore it
					continue;
				if(c == '(') //Push (
					operators.push('(');
				else if(c == ')') //Pop all operators in between ( and )
				{
					while (operators.peek() != '(')
						postfix.add(operators.pop());
					operators.pop(); //This will move the '(' to close ')'
				}
				else
				{
					//while (!operators.isEmpty() && Operator.compare(new Operator(opType.ADD), new Operator(opType.SUB)) <= 0)
					//while not empty and the compare precedence were above 0, then pop.
					//Didn't know how to do this correctly so the output is going to be incorrect.
					while (!operators.isEmpty())
						postfix.add(operators.pop());
					operators.push(c);
				}
			}
		}
		if(stackOperand) //add to stack what's left
			postfix.add(stack);
		
		while(!operators.isEmpty()) // Move just as above
			postfix.add(operators.pop());
		return postfix;
	}
		static int evalPostfix(List<Object> postfix) //evaluate the postfix
		{
			Stack<Integer> operands = new Stack<Integer>();
			int a = 0; //Left variable
			int b = 0; // right variable
			for (Object s : postfix) {
				if(s instanceof Character)//if Object s is an instance of Character
				{
					char c = (Character) s;
					b = operands.pop();
					a = operands.pop();
					//Math
					if(c == '+')//Didn't have time to try opType.ADD/SUB/MULT/DIV/MOD here
						operands.push(a + b);
					else if (c == '-')
						operands.push(a - b);
					else if (c == '%')
						operands.push(a % b);
					else if (c == '*')
						operands.push(a * b);
					else
						operands.push(a / b);				
				}
				else 
				{ // instance of Integer
					operands.push((Integer)s);
				}
			}
			return operands.pop();
		}
		
    public static void main(String result) throws FileNotFoundException //This is the main function
    {
    	File text = new File("input.infix"); //hardcoded input.infix file as asked
    	Scanner input = new Scanner(text);
    	if(input.hasNextLine())//in case input.infix doesn't work on me
    	{
    		while(input.hasNextLine())
    		{
    			String value = input.nextLine();
    			System.out.println(value);
    			//print input
    			List<Object> iExpr = infix2Postfix(value); //get variable for infix
    			//print on the next line the infix = postfix
    			System.out.printf("%n", iExpr, " = ", evalPostfix(iExpr));
    		}
    	}
    	else //If input.infix doesn't work as expected manual inputs will be needed.
    	{
    		System.out.println("Enter your numbers ");
    		String name = System.console().readLine(result);
    		List<Object> iExpr = infix2Postfix(name); 
    		System.out.printf(result, "%n", iExpr, " = ", evalPostfix(iExpr));
    	
    	}
    	input.close();
    }
}
    


