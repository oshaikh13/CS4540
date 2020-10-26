import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.FileReader;
import java.util.StringTokenizer;
import java.util.HashMap;
import java.util.Set; 
import java.util.ArrayList; 


public class Q3 {
    public static int[] dp;
    public static int[] parity;
    public static HashMap<Integer, ArrayList<Integer>> adj;


    public static int dfsA(int currNode, int currParity) {
        dp[currNode] += parity[currNode];
        
        if (adj.containsKey(currNode)) {
            for (int nextNode : adj.get(currNode)) { 
                if ((nextNode ^ currParity) != 0) {
                    int ret = dfsA(nextNode, currNode);
                    if ((parity[nextNode] ^ parity[currNode]) != 0) {
                        dp[currNode] += ret;
                    }
                }
            }
        }

        return dp[currNode];
    }

    public static void dfsB(int currNode, int currParity) {
        if (currParity != -1 && parity[currParity] != parity[currNode]) {
            dp[currNode] += dp[currParity] - dp[currNode];
        }

        if (adj.containsKey(currNode)) {
            for (int nextNode : adj.get(currNode)) {
                if ((nextNode ^ currParity) != 0) {
                    dfsB(nextNode, currNode);
                }
            }
        }
    }


    public static void solve() {

        dfsA(1, -1);
        dfsB(1, -1);

        long ans = 0;
        for (int i = 1; i < dp.length; i++) {
            ans += dp[i];
        }
        System.out.println(ans);
    }

    public static void main(String [] args) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());

            parity = new int[n + 1];
            dp = new int[n + 1];
            adj = new HashMap<>();

            st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= n; i++) {
                parity[i] = Integer.parseInt(st.nextToken()) & 1;
            }

            for (int i = 1; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                if (!adj.containsKey(a)) {
                    adj.put(a, new ArrayList<Integer>());
                }

                if (!adj.containsKey(b)) {
                    adj.put(b, new ArrayList<Integer>());
                }

                adj.get(a).add(b);
                adj.get(b).add(a);
            }

        } catch (Exception e) {
            System.out.println(e);
        }
        
        solve();

    }
}