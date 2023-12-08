package base_java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CombineGroupSet {

    public void CombineDim(int[] sourceList, int dimNum, int groupNum, int[] tmpResult, int subn) {
        List<Integer> res = new ArrayList<>();
        if (groupNum == 0) { //出口
            for (int i = 0; i < subn; ++i) {
                res.add(tmpResult[i]);
                System.out.print(tmpResult[i]);
            }
            System.out.println();
            System.out.println(res);
        } else {
            for (int i = dimNum; i >= groupNum; --i) { // 从后往前依次选定一个
                tmpResult[groupNum - 1] = sourceList[i - 1]; // 选定一个后
                CombineDim(sourceList, i - 1, groupNum - 1, tmpResult, subn); // 从前i-1个里面选取m-1个进行递归
            }
        }
    }

    public void Combine(String sourceDim, String bindDim) {
        List sourceDimList = new ArrayList(Arrays.asList(sourceDim.split(",")));
        System.out.println(sourceDimList);
        List bindDimList = new ArrayList(Arrays.asList(bindDim.split(",")));
        System.out.println(bindDimList);
        List<Integer> sourceIndex = new ArrayList();
        List<Integer> bindIndex = new ArrayList();
        List<Integer> groupIndex = new ArrayList();
      //  int[] sourceIndex, bindIndex, groupIndex = new int[sourceDimList.size()];
        for (int i = 0; i < sourceDimList.size(); i++) {
            sourceIndex.add(i);
            System.out.println(sourceDimList.get(i));
            for (int j = 0; j < bindDimList.size(); j++) {
                System.out.println(bindDimList.get(j));
                if (sourceDimList.get(i).equals(bindDimList.get(j))) {
                    System.out.println(sourceDimList.get(i));
                    bindIndex.add(i);
                }
                else {
                    groupIndex.add(i);
                }
            }

        }

        System.out.println("sourceIndex: " + sourceIndex);
        System.out.println("bindIndex: " + bindIndex);
        System.out.println("groupIndex: " + groupIndex);



    }

    public static void main(String[] args) {
        CombineGroupSet comb = new CombineGroupSet();
        comb.Combine("os,groupname,platform,is_pay,invl,cycle", "invl");
    }
}
