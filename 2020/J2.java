import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int P = in.nextInt();
        int N = in.nextInt();
        int R = in.nextInt();

        int ip=N;
        int ild=N;
        int count=0;

        while (P>=ip){
          count++;
          ip+=ild*R;
          ild*=R;
        }

        
        System.out.print(count);
        
    }
}
