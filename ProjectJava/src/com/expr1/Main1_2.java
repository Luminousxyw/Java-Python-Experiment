import java.util.Scanner;
public class Main1_2 {
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);
        int a=scanner.nextInt();
        int b=scanner.nextInt();
        int c=scanner.nextInt();
        if(a<=b){
            System.out.println(a<c?a:c);
        }
        else{
            System.out.println(b<c?b:c);
        }
    }
}
