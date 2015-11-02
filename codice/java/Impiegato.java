
public class Impiegato implements IImpiegato{
	private String nome;
	private String cognome;
	private double stipendio;

	public Impiegato(String cognome, String nome, double stipendio) {
		this.nome = nome;
		this.cognome = cognome;
	}

	public double getStipendio() {
		return stipendio;
	}

	public void setStipendio(double d) {
		this.stipendio = d;
	}

	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getCognome() {
		return cognome;
	}
	public void setCognome(String cognome) {
		this.cognome = cognome;
	}
	
}
