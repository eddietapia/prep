/*
Given two strings, base and remove, return a version of the base string where all instances of the remove string have been removed (not case sensitive). You may assume that the remove string is length 1 or more. Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".


withoutString("Hello there", "llo") → "He there"
withoutString("Hello there", "e") → "Hllo thr"
withoutString("Hello there", "x") → "Hello there"
*/
public String withoutString(String base, String remove) {
  char[] baseArray = base.toCharArray();
  char[] removeArray = remove.toCharArray();
  String output = new String();
  
  int rSize = remove.length() - 1;
  int rCounter = 0;
  String temp = new String();
  
  for (char c: baseArray){
    if (Character.toLowerCase(c) == Character.toLowerCase(removeArray[rCounter])){
      if (rCounter == rSize){
        // Do not add the current letters to the output
        temp = "";
        rCounter = 0;
      }
      else{
        temp += c;
        rCounter++;
      }
    }
    else{
      output = output.concat(temp + c);
      temp = "";
      rCounter = 0;
    }
  }
  if (!temp.equals("")){
    output += temp;
  }
  return output;
}

