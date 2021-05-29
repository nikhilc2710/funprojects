import java.util.*;  
class Main{
    public static String sortString(String s){
         char[] chars = s.toCharArray();
        Arrays.sort(chars);
        String sorted = new String(chars);
        return sorted;
    }
    public static void main(String args[]){
    ArrayList<String> list = new ArrayList<String>();   
    list.add("Computer");  
    list.add(String.valueOf(123));   
    list.add("Hard Disk");  
    list.add("DRAM");  
    Collections.sort(list);   
    for (String i:list){
        System.out.println((sortString(i)));
        }
    }
    
}
