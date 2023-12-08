package base_java;

import java.util.ArrayList;
import java.util.List;

public class CombinationList {
    private static final int DEFAULT_MAX=5;
    private static final int DEFAULT_SORT_SIZE=3;
    static void com(int numbers[],int m){
        int n=numbers.length;
        if(m>n) return;

        int temp[]=new int[10],i,k=0;

        for(i=0;i<m;i++) temp[i]=-1;

        temp[k]=0;
        // 核心算法
        while(true){
            if(temp[k]>=n)  //n 是原始数组长度
            {
                if(k==0) break;
                --k;
                temp[k]+=1;
            }
            else if(k==m-1)
            {
                for(int j=0;j<m;j++) System.out.print(numbers[temp[j]]  +" ");
                System.out.println();
                temp[k]+=1;
            }
            else{
                ++k;
                temp[k]=temp[k-1]+1;
            }

        }

    }

    void combination(int[] chars, int n, int m, int[] subchars, int subn) {
        List<Integer> res = new ArrayList<>();
        if (m == 0) { //出口
            for (int i = 0; i < subn; ++i) {
                res.add(subchars[i]);
                System.out.print(subchars[i]);
            }
            System.out.println();
            System.out.println(res);

        } else {
            for (int i = n; i >= m; --i) { // 从后往前依次选定一个
                subchars[m - 1] = chars[i - 1]; // 选定一个后
                combination(chars, i - 1, m - 1, subchars, subn); // 从前i-1个里面选取m-1个进行递归
            }
        }
       // return res;
    }

    public static void main(String[] args) {
        int numbers[]={1,2,3,4,5};
        int result[] = new int[5];
        CombinationList cl = new CombinationList();
        for(int i=1;i<=DEFAULT_SORT_SIZE;i++){
             com(numbers, i);
           // cl.combination(numbers, numbers.length, i, result, i);
        }
        System.out.println("********* 分割线 *********");
        List<Integer> finalres = new ArrayList();
        //cl.combination(numbers, numbers.length, 2, result, 2);
        //System.out.println("finalres" + finalres);
    }
}
