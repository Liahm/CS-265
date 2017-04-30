/*
@Name: Eric Lee
@Date: 11/20/2016
@platform: tux on drexel.edu
@Description: Provides the ability to parse, add, multiply and find the normal of gaussian integers.
*/
import java.lang.Math;

public class gInt
{
	public int a = 0;
	public int b = 0;

	public static void main(String[] args){
	}
	//Real only
	public gInt(int real)
	{
		a = real;
	}
	//Both constructor
	public gInt(int real,int imaginary)
	{
		a = real;
		b = imaginary;
	}
	
	//Real Gaussian Int
	public int real()
	{
		return a;
	}
	
	//imaginary Gaussian Int
	public int imaginary()
	{
		return b;
	}

	//Add method
	public gInt add(gInt x)
	{
		//Formula for add is (a+c) + (b+d)i
		gInt result = new gInt((a + x.real()),(b + x.imaginary()));
		return result;
	}
	
	//Multiplication method
	public gInt multiply(gInt x)
	{
		//Formula for mult is (ac-bd)+(ad+bC)i
		gInt product = new gInt((a * x.real()) - (b * x.imaginary()), (a* x.imaginary()+(b * x.real())));
		return product;
	}
	//Calculate normal of Gaussian Integer, the L2
	public float norm()
	{
 		return (float)Math.sqrt((a*a)+(b+b));
	}

	//Equals
	public boolean equals(Object anObject)
	{
		if( anObject instanceof gInt)
		{
			gInt agInt=(gInt)anObject;
			return (agInt.real()==real() && agInt.imaginary()==imaginary());
		}
		return false;
	}
}

