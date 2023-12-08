package base_java;

public class TestDemo {
    public static void main(String[] args) {
        int MAX_NUM = 0;
        for (int i = 0; i < MAX_NUM; i++) {
            System.out.println("aaa"+i);
        }

        String s_dim = "os,groupname,platform";
        String[] s_arr = s_dim.split(",");
        System.out.println(s_arr);
    }
}
