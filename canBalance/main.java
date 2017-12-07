/*
Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers on one side is equal to the sum of the numbers on the other side.


canBalance([1, 1, 1, 2, 1]) → true
canBalance([2, 1, 1, 2, 1]) → false
canBalance([10, 10]) → true

*/
public boolean canBalance(int[] nums) {
  int currentBalance = 0;
  for (int i = 0; i < nums.length; i++) {
    currentBalance += nums[i];
    int rightBalance = 0;
    for (int j=i+1; j < nums.length; j++) {
      rightBalance += nums[j];
    }
    if (currentBalance == rightBalance) {
      return true;
    }
  }
  return false;
}
