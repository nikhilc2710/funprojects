import java.util.ArrayList;
class Main{
    public static void main(String args[]){
    ArrayList<Integer> arr = new ArrayList<Integer>();
    int st=1215598;
    String temp=String.valueOf(st);
    int ans=0;
    int n=temp.length();
    for (int i=0;i<n;i++){
        for (int j=i+1;j<=n;j++){
            if (Integer.parseInt(temp.substring(i,j))%11==0){
                System.out.print(temp.substring(i,j)+" ");
                ans+=1;
            }
        }
    }
    System.out.println(ans);
    
    
    }
}
