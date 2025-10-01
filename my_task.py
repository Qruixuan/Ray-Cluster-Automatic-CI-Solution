from prometheus_client import start_http_server, Gauge
import math
import time

# 创建一个 Gauge 指标
ray_test_metric = Gauge('ray_test_metric', 'A test metric from Ray cluster')

def generate_metrics():
    t = 0
    while True:
        # 正弦函数：结果在 0~100 之间
        value = (math.sin(t) + 1) * 50
        ray_test_metric.set(value)
        print(f"Updated ray_test_metric = {value:.2f}")

        time.sleep(1)
        t += 0.1

if __name__ == '__main__':
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000")
    generate_metrics()
