
public class AdaptedEmployer implements IImpiegato {
	
	Employer employer;
	
	public AdaptedEmployer(Employer employer) {
		this.employer = employer;
	}

	
	@Override
	public String getNome() {
		return employer.getName();
	}
	@Override
	public String getCognome() {
		return employer.getLastName();
	}
	@Override
	public double getStipendio() {
		return employer.getSalary()/0.7171;
	}

	@Override
	public void setCognome(String cognome) {
		employer.setLastName(cognome);		
	}
	@Override
	public void setNome(String nome) {
		employer.setName(nome);
		
	}
	@Override
	public void setStipendio(double stipendio) {
		employer.setSalary(stipendio);
		
	}
	
}
