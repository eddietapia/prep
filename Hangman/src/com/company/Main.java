package com.company;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class Main {
    static String word;
    static int[] wordTable;
    static int wrongCount;
    static boolean won;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
	    System.out.println("Welcome to hangman!");
	    HangmanLexicon lexicon = new HangmanLexicon();
	    // Generate random index for word
        int wordIndex = ThreadLocalRandom.current().nextInt(0, lexicon.getWordCount() + 1);
	    // Get the word at the random index
        word = lexicon.getWord(wordIndex);

        // Initialize game conditions
        wrongCount = 0;
        won = false;

        wordTable = new int[word.length()];

        // Keep playing game until user loses or wins
        while(wrongCount < 8 && !won){
            getStatus(wordTable);
            System.out.println("\nYou have "+ (8-wrongCount) + " guesses left.");
            processInput(scanner);

            // Check if the user has won
            if(hasWon()){
                won = true;
            }
        }
        if(won) {
            System.out.println("You guessed the word: " + word);
            System.out.println("You win.");
            return;
        }
        System.out.println("You're completely hung.");
        System.out.println("The word was: " + word );
        System.out.println("You lose.");
        return;
    }

    public static void getStatus(int[] wordTable){
        System.out.print("The word now looks like this: ");
        for (int i = 0; i < word.length(); i++) {
            if (wordTable[i] == 1){
                System.out.print(word.charAt(i) + " ");
            }
            else{
                System.out.print("_ ");
            }
        }
    }

    public static boolean hasWon(){
        for(int i = 0; i < wordTable.length; i++){
            if(wordTable[i] == 0){
                return false;
            }
        }
        return true;
    }

    public static void processInput(Scanner scanner){
        boolean hit = false;
        String guess = scanner.nextLine().toUpperCase();
        System.out.println("Your guess: " + guess);
        if (guess.length() > 1 || guess.length() == 0){
            System.out.println("Please choose one letter at a time.");
            wrongCount++;
            return;
        }
        else{
            // Iterate the word to see if there is a match
            for(int i = 0; i < word.length(); i++) {
                if (guess.charAt(0) == word.charAt(i)){
                    hit = true;
                    wordTable[i] = 1;
                }
            }
        }
        if(hit){
            System.out.println("That guess is correct.");
            return;
        }
        System.out.println("There are no " + guess + "'s in the word.");
        wrongCount++;
    }
}
