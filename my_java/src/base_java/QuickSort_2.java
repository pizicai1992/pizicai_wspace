package base_java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @version v1.0
 * @ProjectName: my_java
 * @ClassName: QuickSort_2
 * @Description: TODO(一句话描述该类的功能)
 * @Author: 蔡牙
 * @Date: 2020/7/2/0002 0:26
 */
public class QuickSort_2 {
    private static List<Integer> quickSort(List<Integer> list){
        List<Integer> left = new ArrayList<>() ;
        List<Integer> right = new ArrayList<>();
        if (list.size() < 2) {
            return list;
        }else {
            int baseNum = list.get(0);
            for (int i = 1; i < list.size(); i++) {
                if (list.get(i) < baseNum) {
                    left.add(list.get(i));
                }else {
                    right.add(list.get(i));
                }
            }
            return quickSort(left);
        }
    }

    public static void main(String[] args) {
        int[] aa = {49, 38, 65, 97, 23, 22, 76, 1, 5, 8, 2, 0, -1, 22} ;
        List arr = new ArrayList(Arrays.asList(aa));
        //Integer[] res = quickSort(arr);
        System.out.println(arr.toString());
        //System.out.println(res.toString());
    }
}
