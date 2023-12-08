package base_java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @version v1.0
 * @ProjectName: my_java
 * @ClassName: QuickSort
 * @Description: Java实现快速排序算法
 * @Author: 蔡牙
 * @Date: 2020/7/1/0001 22:16
 */
public class QuickSort {
    public static Integer[] quickSort(Integer[] arr){
        int baseNum = 0;

        Integer[] leftArray = {};
        List<Integer> lList = Arrays.asList(leftArray);
        List<Integer> leftList = new ArrayList(lList);
        Integer[] rightArray = {};
        List<Integer> rList = Arrays.asList(rightArray) ;
        List<Integer> rightList = new ArrayList(rList);
        List<Integer> resultList = new ArrayList();
        if (arr.length < 2) {
            return arr;
        } else {
            baseNum = arr[0];
            for (int i = 1; i < arr.length; i++) {
                if (arr[i] < baseNum) {
                    leftList.add(arr[i]);
                }else rightList.add(arr[i]);
            }
            Integer[] newLeft = new Integer[leftList.size()];
            Integer[] newRight = new Integer[rightList.size()];
            leftList.toArray(newLeft);
            rightList.toArray(newRight);
            List<Integer> resL = new ArrayList<Integer>(Arrays.asList(quickSort(newLeft)));
            resultList.addAll(resL);
            resultList.add(baseNum);
            List<Integer> resR = new ArrayList<Integer>(Arrays.asList(quickSort(newRight)));
            resultList.addAll(resR);
            rightList.clear();
            leftList.clear();
            Integer[] resultArray = new Integer[resultList.size()];
            resultList.toArray(resultArray);
            System.out.println(resultArray.toString());
            resultList.clear();
            //return quickSort(resultArray);
            return resultArray;
        }
    }

    public static void main(String[] args) {
        Integer[] arr = {49, 38, 65, 97, 23, 22, 76, 1, 5, 8, 2, 0, -1, 22};
        Integer[] res = quickSort(arr);
        System.out.println(arr.toString());
        System.out.println(res.toString());
    }
}
