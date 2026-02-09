import java.util.Random;
import java.util.Scanner;

public class game {

    public static final int BJORKSNAS = 0;
    public static final int FJALLBO = 1;
    public static final int SODERHAMN = 2;
    public static final int GRONLID = 3;
    public static final int TORNVIKEN = 4;

    public static final int MOVE_COUNT = 5;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int rounds = 0;
        int userWins = 0;
        int computerWins = 0;

        printRules();

        while (askToPlay(scanner)) { //use while loops
            int userMove = getUserMove(scanner);
            int computerMove = getComputerMove(random);

            echoMove("Your move is", userMove);
            echoMove("Computer move is", computerMove);

            int result = determineWinner(userMove, computerMove);

            if (result == 1) {
                System.out.println("You win this round!");
                userWins++; //for +=1 use ++ instead
            } else {
                System.out.println("Computer wins this round!");
                computerWins++;
            }

            rounds++;
        }

        printStats(rounds, userWins, computerWins);
        scanner.close();
    }

    public static void printRules() {
        System.out.println("Game Rules:");
        System.out.println("Fjallbo beats Soderhamn, Tornviken");
        System.out.println("Soderhamn beats Bjorksnas, Gronlid");
        System.out.println("Bjorksnas beats Fjallbo, Tornviken");
        System.out.println("Tornviken beats Gronlid, Soderhamn");
        System.out.println("Gronlid beats Fjallbo, Bjorksnas");
        System.out.println();
    }

    public static boolean askToPlay(Scanner scanner) {
        while (true) {
            System.out.print("Would you like to play a round? (y/n): ");
            String input = scanner.nextLine().toLowerCase();
            System.out.println("You entered: " + input);

            if (input.equals("y")) return true;
            if (input.equals("n")) return false;

            System.out.println("Invalid input. Try again.");
        }
    }

    public static int getUserMove(Scanner scanner) {
        while (true) {
            System.out.print("Enter your move (Bjorksnas, Fjallbo, Soderhamn, Gronlid, Tornviken): ");
            String move = scanner.nextLine().toLowerCase();
            System.out.println("You entered: " + move);

            switch (move) {
                case "bjorksnas": return BJORKSNAS;
                case "fjallbo": return FJALLBO;
                case "soderhamn": return SODERHAMN;
                case "gronlid": return GRONLID;
                case "tornviken": return TORNVIKEN;
                default:
                    System.out.println("Invalid move. Try again.");
            }
        }
    }

    public static int getComputerMove(Random random) {
        return random.nextInt(MOVE_COUNT);
    }

    public static int determineWinner(int user, int computer) {
        if (user == computer) return 0;

        if (
            (user == FJALLBO && (computer == SODERHAMN || computer == TORNVIKEN)) || //dictionary in java 
            (user == SODERHAMN && (computer == BJORKSNAS || computer == GRONLID)) ||
            (user == BJORKSNAS && (computer == FJALLBO || computer == TORNVIKEN)) || //&& translate for and statement 
            (user == TORNVIKEN && (computer == GRONLID || computer == SODERHAMN)) || //use || for or statement replacement like how == is replaced by .equal()
            (user == GRONLID && (computer == FJALLBO || computer == BJORKSNAS))
        ) {
            return 1;
        }

        return 0;
    }

    public static void echoMove(String text, int move) {
        System.out.println(text + " " + moveToString(move));
    }

    public static String moveToString(int move) {
        switch (move) {//switch is the shorter vwersion for else if statement for multiple dictionary like this
            case BJORKSNAS: return "Bjorksnas";//you don't have to type if()
            case FJALLBO: return "Fjallbo";//no need to type else if()
            case SODERHAMN: return "Soderhamn";//just type switch(move from user input) go to getUsetMove() int funcion
            case GRONLID: return "Gronlid"; // while using switch, you need case like naming a type from variables 
            case TORNVIKEN: return "Tornviken";
            default: return "Unknown";//else Unknown
        }
    }

    public static void printStats(int rounds, int userWins, int computerWins) {
        System.out.println();
        System.out.println("Rounds played: " + rounds);
        System.out.println("User wins: " + userWins);
        System.out.println("Computer wins: " + computerWins);
        System.out.println("Game over.");
    }
}
