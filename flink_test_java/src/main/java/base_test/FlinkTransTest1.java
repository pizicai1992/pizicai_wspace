package base_test;

import org.apache.flink.api.common.functions.MapFunction;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.functions.source.SourceFunction;

/**
 * @version v1.0
 * @ProjectName: flink_test_java
 * @ClassName: FlinkTransTest1
 * @Description: Flink转换算子
 * @Author: 蔡牙
 * @Date: 2021-12-17 23:34
 */
public class FlinkTransTest1 {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        String filePath = "F:\\My_WorkSpace\\flink_test_java\\src\\main\\resources\\wordlist.text";
        DataStreamSource<String> inputStream = env.readTextFile(filePath);

        // inputStream.print();
        DataStream<Integer> mapStream = inputStream.map(new MapFunction<String, Integer>() {
            @Override
            public Integer map(String s) throws Exception {
                return s.length();
            }
        });



        mapStream.print();
        env.execute();


    }

//    public static class MyTest implements SourceFunction<String> {
//
//        @Override
//        public void run(SourceContext<String> sourceContext) throws Exception {
//
//        }
//
//        @Override
//        public void cancel() {
//
//        }
//    }
}
