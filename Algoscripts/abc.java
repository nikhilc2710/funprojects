import java.util.*;
class Main {
            static boolean checkPrime(int n){
             boolean flag = false;
            for (int i = 2; i <= n / 2; ++i) {
      
            if (n % i == 0) {
            flag = true;
            break;
        }
        }

        if (!flag){
        return true;}
        else{
        return false;}
            
        }
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        System.out.println("enter Bus no");
        int a =s.nextInt();
        if (checkPrime(a)){
            System.out.println("You can Board bus");
            
        }
        else{
            System.out.println("You cannot board bus");
            main(args);
        }

        
        
     
   
  }

    }
