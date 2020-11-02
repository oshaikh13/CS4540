import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.FileReader;
import java.util.StringTokenizer;

public class Q2 {
    public static long[] tree;
    public static long[] counts;

    public static void update(long x, long v, long[] arr) {
        while (x < arr.length) {
            arr[(int) x] += v;
            x += (x & -x);
        }
    }

    public static long query(long v, long[] arr) {
        long ans = 0;
        while (v > 0) {
            ans += arr[(int) v];
            v -= (v & -v);
        }
        return ans;
    }

    public static void main(String [] args) {
        tree = new long[100100];
        counts = new long[100100];

        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());

            int elems = Integer.parseInt(st.nextToken());
            int queries = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());

            for (int i = 1; i <= elems; i++) {
                long curr_data = Integer.parseInt(st.nextToken());
                update(i, curr_data, tree);
                update(curr_data, 1, counts);
            }

            for (int i = 0; i < queries; i++) {
                st = new StringTokenizer(br.readLine());
                String type = st.nextToken();
                int a = Integer.parseInt(st.nextToken());
                if (type.equals("S")) {
                    int b = Integer.parseInt(st.nextToken());
                    System.out.println(query(b, tree) - query(a - 1, tree));
                } else if (type.equals("C")) {
                    int b = Integer.parseInt(st.nextToken());
                    long queryResult = query(a, tree) - query(a - 1, tree);
                    update(a, b - queryResult, tree);
                    update(queryResult, -1, counts);
                    update(b, 1, counts);            
                } else {
                    System.out.println(query(a, counts));
                }
            }

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}