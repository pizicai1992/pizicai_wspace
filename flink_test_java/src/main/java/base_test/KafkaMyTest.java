package base_test;

import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.datastream.SingleOutputStreamOperator;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumerBase;
import org.apache.flink.util.Collector;

import java.util.Properties;

/**
 * @version v1.0
 * @ProjectName: flink_test_java
 * @ClassName: KafkaMyTest
 * @Description: Flink 连接kafka测试
 * @Author: 蔡牙
 * @Date: 2021-12-23 22:56
 */
public class KafkaMyTest {
    public static void main(String[] args) throws Exception {
        //1. 创建执行环境
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        //2. 连接kafka source
        Properties properties = new Properties();
        properties.setProperty("bootstrap.servers", "192.168.10.10:9092");
        properties.setProperty("group.id", "test");
        properties.setProperty("key.deserializer",
                "org.apache.kafka.common.serialization.StringDeserializer");
        properties.setProperty("value.deserializer",
                "org.apache.kafka.common.serialization.StringDeserializer");
        properties.setProperty("auto.offset.reset", "latest");

        DataStreamSource<String> kafkaStream = env.addSource
                (new FlinkKafkaConsumer<String>("test_flink", new SimpleStringSchema(), properties));

        //3. 转换操作
        SingleOutputStreamOperator<Tuple2<String, Integer>> mapStream =
                kafkaStream.flatMap(new FlatMapFunction<String, Tuple2<String, Integer>>() {
            public void flatMap(String s, Collector<Tuple2<String, Integer>> collector) throws Exception {
                String[] words = s.toLowerCase().split("\\W+");
                for (String word : words) {
                    if (word.length() > 0) {
                        collector.collect(new Tuple2<>(word, 1));
                    }
                }
            }
        });

        SingleOutputStreamOperator<Tuple2<String, Integer>> wordCount = mapStream.keyBy(0).sum(1);

        // 4. 打印结果
        wordCount.print();
        // 5. 开始执行
        env.execute();

    }
}