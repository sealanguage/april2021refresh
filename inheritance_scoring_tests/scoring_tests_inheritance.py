import java.util. *;

class Person {
protected String firstName;
protected String lastName;
protected int idNumber;

// Constructor
Person(String firstName, String lastName, int identification){
this.firstName = firstName;
this.lastName = lastName;
this.idNumber = identification;
}

// Print person data
public void printPerson(){
System.out.println(
"Name: " + lastName + ", " + firstName
+    "\nID: " + idNumber);
}

}


class Student extends Person{
private int[] testScores;

/ *
* Class Constructor
*
* @ param firstName - A string denoting the Person's first name.
* @ param lastName - A string denoting the Person's last name.
* @ param id - An integer denoting the Person's ID number.
* @ param scores - An array of integers denoting the Person's test scores.
* /
// Write your constructor here
public Student(String lastName, String firstName, int idNumber, int[] testScores) {
super(lastName, firstName, idNumber);
this.testScores = testScores;
}

/ *
* Method Name: calculate
               * @


return A
character
denoting
the
grade.
* /
// Write
your
method
here
public
char
calculate()
{
    int
total = 0;

for (int idx = 0; idx < testScores.length; idx++) {
    total += testScores[idx];
}
total /= testScores.length;

if (total >= 90)
    return 'O';
if (total >= 80)
    return 'E';
if (total >= 70)
    return 'A';
if (total >= 55)
    return 'P';
if (total >= 40)
    return 'D';

return 'T';

}
}

class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in );
        String firstName = scan.next();
        String lastName = scan.next();
        int id = scan.nextInt();
        int numScores = scan.nextInt();
        int[] testScores = new int[numScores];
            for (int i = 0; i < numScores; i++){
            testScores[i] = scan.nextInt();
    }
    scan.close();

Student s = new Student(firstName, lastName, id, testScores);
s.printPerson();
System.out.println("Grade: " + s.calculate() );
}
}