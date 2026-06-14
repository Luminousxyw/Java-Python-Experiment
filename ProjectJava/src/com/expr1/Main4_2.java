import java.util.Scanner;
public class Main4_2 {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int n;
        do{
            System.out.print("please enter a num : ");
            n=scanner.nextInt();
        }while(n<30||n>80);
        int i,sum=0;
        for(i=0;i<=n;i++){
            sum+=i;
        }
        System.out.println(sum);
    }
}
