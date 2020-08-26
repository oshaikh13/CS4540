import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Arrays;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.FileReader;
import java.util.StringTokenizer;


// something something gave up on python something something.
public class p3 {
    public static void main(String[] args) {


        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            int cases = -1;
            StringTokenizer st = new StringTokenizer(br.readLine());

            cases = Integer.parseInt(st.nextToken());

            for (int i = 0; i < cases; i++) {
                String curr = br.readLine();
                st = new StringTokenizer(curr);
                int m = Integer.parseInt(st.nextToken());
                int n = Integer.parseInt(st.nextToken());
                int f = Integer.parseInt(st.nextToken());
                int k = Integer.parseInt(st.nextToken());

                float [][] stations = new float[m + 1][n + 1];

                for (float[] t1 : stations) {
                    Arrays.fill(t1, -1);
                }

                for (int j = 0; j < k; j++) {
                    st = new StringTokenizer(br.readLine());
                    int a = Integer.parseInt(st.nextToken());
                    int b = Integer.parseInt(st.nextToken());   
                    float cost = Float.parseFloat(st.nextToken());
                    if (stations[a][b] == -1 || stations[a][b] > cost ) {
                        stations[a][b] = cost;
                    }
                }
                solve(m, n, f, stations);
            }

        } catch (Exception e) {
            System.out.println(e);

        }




    }


    public static void solve(int m, int n, int f, float [][] stations) {

        float [][][] dp = new float[m + 1][n + 1][f + 1];

        for (float[][] t1 : dp) {
            for (float[] t2 : t1) {
                Arrays.fill(t2, Float.MAX_VALUE);
            }
        }

        dp[1][1][f] = 0;

        // i know, i'm sorry :'(
        PriorityQueue<float[]> heap = new PriorityQueue((a, b) -> {
            float costA = ((float[])a)[0];
            float costB = ((float[])b)[0];
            if (costA - costB > 0) return 1;
            else if (costA == costB) return 0;
            return -1;
        });

        // (priority, m, n, f)
        heap.add(new float[]{0, 1, 1, f});

        int currM, currN, currF;
        currM = currN = currF = -1;

        while (heap.size() > 0) {
            float [] currState = heap.poll();
            float currCost = currState[0];
            currM = (int) currState[1];
            currN = (int) currState[2];
            currF = (int) currState[3];

            // we can break since this is p much just djikstra, and we know
            // if we hit the node for the first time, we're done.
            if (currM == m && currN == n) break;
            
            if (currCost > dp[currM][currN][currF]) continue;

            int [][] delta = 
                new int [][] { {-1, 0}, {0, -1}, {0, 0}, {0, 1}, {1, 0} };
            
            for (int[] currDelta : delta) {
                int dm = currDelta[0];
                int dn = currDelta[1];

                int newF = currF;
                int newM = currM;
                int newN = currN;
                float newCost = currCost;

                if (dm == 0 && dn == 0) {
                    if (++newF > f || stations[newM][newN] == -1) continue;
                    newCost += stations[newM][newN];
                    if (newCost >= dp[newM][newN][newF]) continue;
                    heap.add(new float[]{newCost, newM, newN, newF});
                    dp[newM][newN][newF] = newCost;
                } else {
                    newM += dm;
                    newN += dn;

                    // out of bounds
                    if (newM > m || newM < 1 || newN > n || newN < 1 || --newF < 0)
                        continue;
                
                    heap.add(new float[]{newCost, newM, newN, newF});
                    dp[newM][newN][newF] = newCost;
                }
            }

        }

        if (currM == m && currN == n) {
            System.out.printf("%.2f\n", dp[m][n][0]);
        } else {
            System.out.println("Stranded on the shoulder");
        }

    }
}