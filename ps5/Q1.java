import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.FileReader;
import java.util.StringTokenizer;

public class Q1 {

    private static int [] tree = new int[400000];
    private static int [] data = new int[110000];

    public static void build(int idx, int start, int end) {
        if (start == end) {
            tree[idx] = data[end];
            return;
        }

        int mid = (start + end) / 2;
        build(2 * idx + 1, start, mid);
        build(2 * idx + 2, mid + 1, end);
        tree[idx] = Math.min(tree[2 * idx + 1], tree[2 * idx + 2]);

    }

    public static int query(int l, int r, int idx, int start, int end) {
        if (r < start || l > end) {
            return Integer.MAX_VALUE;
        }

        if (r >= end && l <= start) {
            return tree[idx];
        }

        int mid = (start + end) / 2;
        int left = query(l, r, 2 * idx + 1, start, mid);
        int right = query(l, r, 2 * idx + 2, mid + 1, end);
        return Math.min(left, right);
    }

    public static void update(int i, int x, int idx, int start, int end) {
        if (start == end) {
            data[i] = x;
            tree[idx] = x;
            return;
        }

        int mid = (start + end) / 2;
        if (start <= i && i <= mid) {
            update(i, x, 2 * idx + 1, start, mid);
        } else update(i, x, 2 * idx + 2, mid + 1, end);

        tree[idx] = Math.min(tree[2 * idx + 1], tree[2 * idx + 2]);
    }

    public static void main(String [] args) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            int elems = -1;
            int queries = -1;
            StringTokenizer st = new StringTokenizer(br.readLine());

            elems = Integer.parseInt(st.nextToken());
            queries = Integer.parseInt(st.nextToken());

            for (int i = 0; i < elems; i++) {
                st = new StringTokenizer(br.readLine());
                data[i] = Integer.parseInt(st.nextToken());
            }

            build(0, 0, elems - 1);
            for (int i = 0; i < queries; i++) {
                st = new StringTokenizer(br.readLine());
                String type = st.nextToken();
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                if (type.equals("Q")) {
                    System.out.println(query(a, b, 0, 0, elems - 1));
                } else {
                    update(a, b, 0, 0, elems - 1);
                }
            }

        } catch (Exception e) {
            System.out.println(e);

        }
    }
}
