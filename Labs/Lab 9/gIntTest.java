import junit.framework.*;

public class gIntTest extends TestCase
{
	private gInt sum1, sum2;
	private gInt prod1, prod2;
	private gInt normN;

	public gIntTest(String name)
	{
		super(name);
	}

	public static Test Suite()
	{
		return new TestSuite(gIntTest.class);
	}
	protected void setUp()
	{
		gInt1 = new gInt(3, 4);//the L2 should be 5 
		gInt2 = new gInt(9, 16);//the L2 should be 25
	}

	public void testEquals()
	{
		gInt expected = new gInt( 3,4 );
		Assert.assertEquals( expected,gInt1 );
		Assert.assertEquals( gInt1, gInt1 );
		Assert.assertNotSame( expected, gInt1 );
		Assert.assertFalse( gInt1.equals( gInt2 ));
		Assert.assertFalse( expected.equals( gInt2 ));
	}

	public void testAdd()
	{
		gInt checkAdd = new gInt(12, 20);
		gInt sum = gInt1.add(gInt2);
		Assert.assertEquals(checkAdd, sum);		
	}

	public void testMult()
	{
		gInt checkMult = new gInt(-37,84);
		gInt prod = gInt1.multiply(gInt2);
		Assert.assertEquals(checkMult, result);	
	}

	public void testNorm()
	{
		float checkNorm = 5;
		float result = gInt1.norm();
		Assert.assertEquals(checkNorm, result);
	}
	public static void main(String args[])
	{
		junit.textui.TestRunner.run(suite());
	}

}
