
public class tri_fusion {
	
	public static void fusion(int[] A,int deb,int mil,int fin) {
		int n1,n2,i,j;
		int[] R = new int[50]; //tableau tmp
		int[] L = new int[50];// tableau tmp
		n1= mil-deb+1;
		n2= fin -mil;
		for(i=0;i<=n1;i++) L[i]=A[deb+i-1];
		for(j=0;j<=n2;j++) L[j]=A[deb+j];
		L[n1+1]=9999;
		R[n2+1]=9999;
		i=j=0;
		for(int k= deb;k<=fin;k++) {
			if(L[i]<R[j]) {
				A[k]=L[i];
				i++;
			}else {
				A[k]=R[j];
				j++;
			}
		}
	}
	
	public static void decoupe(int[] A, int deb,int fin) {
		int milieu;
		if(deb<fin) {
			milieu = (deb+fin)/2;
			decoupe(A,deb,milieu);
			decoupe(A,milieu+1,fin);
			fusion(A,deb,milieu,fin);
		}
	}
	
	public static void afficher(int[] A,int taille) {
		for(int i=0;i<=taille;i++) {
			System.out.print(" "+A[i]+" ");
		}
	}
	
	
	public static void main(String[] args) {
		int[] A = {38,27,43,3,9,82,10};
		
		System.out.println("Le tableau au depart:");
		afficher(A,A.length-1);
		decoupe(A,1,A.length);
		System.out.println("\n Le tableau apres tri fusion:");
		afficher(A,A.length-1);
	}

}
