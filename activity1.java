import java.util.Scanner;

public class activity1 {
    public static void main (String [] args){
        Scanner input = new Scanner (System.in);

        System.out.print("Enter value of first number: ");
        double num1 = input.nextDouble();

        System.out.print("Enter value of second number: ");
        double num2 = input.nextDouble();

        System.out.print("""
                \nPick an operator:
                add = Additition
                sub = Subtraction
                mul = Multiplication
                div = Division
                : """);

        String operator = input.next();
  
        double ans = 0;
        boolean validation = true;


        if (operator.equals("add")){
            ans = num1 + num2;  
        } else if (operator.equals("sub")   ){
            ans = num1 - num2;
        } else if (operator.equals("mul")){
            ans = num1 * num2;
        } else if (operator.equals("div")){
            ans = num1 / num2;
        } else{
            System.out.println("Di pwedeng wala sa choices");
            validation = false;
        }


        if (validation) {
            System.out.println("\n================================");
            System.out.println("Num1: " + num1 + "\nNum2: " + num2 + "\nAnswer: " + ans);
            System.out.println("================================");
        }
        input.close();
    }


}