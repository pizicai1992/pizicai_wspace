package base_test;

import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.api.java.DataSet;
import org.apache.flink.api.java.ExecutionEnvironment;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.runtime.executiongraph.Execution;
import org.apache.flink.util.Collector;

/**
 * @version v1.0
 * @ProjectName: flink_test_java
 * @ClassName: WordCount
 * @Description: Flink 入门教程之单词计数
 * @Author: 蔡牙
 * @Date: 2021-12-06 23:45
 */
public class WordCount {
    public static void main(String[] args) throws Exception {
        // 1. 首先设置运行环境
        ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();
        // 2. 输入数据源
        DataSet<String> text = env.fromElements("To be, or not to be,--that is the question:--",
                "Whether 'tis nobler in the mind to suffer",
                "The slings and arrows of outrageous fortune",
                "Or to take arms against a sea of troubles,");
        // 3. 单词切分并且进行分组计算
        DataSet<Tuple2<String, Integer>> counts =
                text.flatMap(new LineSplitter())
                .groupBy(0).sum(1);
        // 4. 打印并执行计算
        counts.print();

    }

    // 定义一个函数，用来怎么切分单词
    /**
     * Implements the string tokenizer that splits sentences into words as a user-defined
     * FlatMapFunction. The function takes a line (String) and splits it into
     * multiple pairs in the form of "(word,1)" (Tuple2&lt;String, Integer&gt;).
     */
    public static final class LineSplitter implements FlatMapFunction<String, Tuple2<String, Integer>>{
        @Override
        public void flatMap(String value, Collector<Tuple2<String, Integer>> out) {
            // 将输入的数据切分成数组
            String[] tokens = value.toLowerCase().split("\\W+");
            // 循环遍历数组，讲每个单词组装成元祖(word, 1)这种样式
            for (String token: tokens
                 ) {
                if (token.length() > 0) {
                        out.collect(new Tuple2<>(token, 1));
                }
            }
        }
    }
}
