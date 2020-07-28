public class Magic8 {
  
  public static void main(String[] args) {
    
  System.out.println("MAGIC 8-BALL:");
     
 int randomNumber = (int) (Math.random() * 8);
//inclusive 0 exclusive 8
 System.out.println(randomNumber);
switch(randomNumber) {
  case 0:
  System.out.println("It is certain");
      break;
case 1:
  System.out.println("It is decidedly so");
      break;
      
case 2:
  System.out.println("Reply hazy, try again.");
      break;
case 3:
  System.out.println("Cannot predict now");
      break;
case 4:
  System.out.println("Do not count on it");
      break;
case 5:
  System.out.println("My sources say no");
      break;
case 6:
  System.out.println("Outlook not so good");
      break;
case 7:
  System.out.println("Signs point to yes");
      break;
  default:
    System.out.println("Signs point to immediate");
      break;
}
      
      }
  
}