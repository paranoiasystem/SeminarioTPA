
public class Employer implements IEmployer{
	private String name;
	private String lastName;
	private double salary;

	public Employer(String lastName, String name, double salary) {
		this.salary = salary;
		this.name = name;
		this.lastName = lastName;
	}

	public Employer() {
	}

	public String getLastName() {
		return lastName;
	}
	public void setLastName(String lastName) {
		this.lastName = lastName;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public double getSalary() {
		return salary;
	}
	public void setSalary(double salary) {
		this.salary = salary;
	}
		
}
