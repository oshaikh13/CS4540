import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.FileReader;
import java.util.StringTokenizer;

public class Q4 {

    public static void main (String [] args) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            int cases = -1;
            StringTokenizer st = new StringTokenizer(br.readLine());

            cases = Integer.parseInt(st.nextToken());

            for (int i = 0; i < cases; i++) {
                String curr = br.readLine();
                int [][] memo = new int[curr.length()][curr.length()];
                System.out.println(curr.length() + solve(memo, curr, 0, curr.length() - 1));
            }

        } catch (Exception e) {
            System.out.println(e);

        }
    }

    public static int solve (int [][] memo, String output, int l, int r) {
        if (l == r) return 2;
        if (l > r) return 0;

        if (memo[l][r] <= 0) {
            memo[l][r] = 2 + solve(memo, output, l + 1, r);
            for (int i = l + 1; i <= r; i++) {
                if (output.charAt(l) == output.charAt(i)) {
                    memo[l][r] = Math.min(memo[l][r], solve(memo, output, i, r) + solve(memo, output, l + 1, i - 1));
                }
            }
        }

        return memo[l][r];

    }
}