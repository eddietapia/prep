/*
Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. A number is a series of 1 or more digit chars in a row. (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)


sumNumbers("abc123xyz") → 123
sumNumbers("aa11b33") → 44
sumNumbers("7 11") → 18
*/
public int sumNumbers(String str) {
  // Check is the string is null
  if (str.length() == 0){
    return 0;
  }
  boolean prevFlag = false;
  String current = "";
  int sum = 0;
  // Iterate the string
  for(int i = 0; i < str.length(); i++){
    char c = str.charAt(i);
    if(Character.isDigit(c)){
      if(prevFlag) {
        current += Character.toString(c);
      }
      else{
        current = Character.toString(c);
      }
      prevFlag = true;
    }
    else{
      if (!current.equals("")) {
        sum += Integer.parseInt(current);
      }
      current = "";
      prevFlag = false;
    }
  }
  if (!current.equals("")) {
    sum += Integer.parseInt(current);
  }
  return sum;
}
