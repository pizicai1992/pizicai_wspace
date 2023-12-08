package base_test;

import base_test.WordCount.LineSplitter;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.api.java.utils.ParameterTool;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.datastream.SingleOutputStreamOperator;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

/**
 * @version v1.0
 * @ProjectName: flink_test_java
 * @ClassName: StreamWordCount
 * @Description: 流处理的Wordcount
 * @Author: 蔡牙
 * @Date: 2021-12-13 23:41
 */
public class StreamWordCount {
    public static void main(String[] args) throws Exception {
        // 1. 创建一个流处理的运行环境
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        // 调整并行度进行测试
        //env.setParallelism(2);

        // 2. 从文件读取数据
        //DataStreamSource<String> inputStream = env.readTextFile("F:\\My_WorkSpace\\flink_test_java\\src\\main\\resources\\wordlist.text");
        // 从socket文本流读取数据

        // 解析程序的输入参数
        ParameterTool parameterTool = ParameterTool.fromArgs(args);
        String myHost = parameterTool.get("host");
        int myPort = parameterTool.getInt("port");
        //DataStream<String> inputStream = env.socketTextStream("localhost", 9999);
        DataStream<String> inputStream = env.socketTextStream(myHost, myPort);
        // 3. 转换、分组、求和
        SingleOutputStreamOperator<Tuple2<String, Integer>> resultStream = inputStream.flatMap(new LineSplitter()).keyBy(0)
                .sum(1);
        // 4. 打印结果
        resultStream.print();
        // 5. 开始执行
        env.execute();
    }
}
