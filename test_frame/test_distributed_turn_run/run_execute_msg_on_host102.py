from test_frame.test_distributed_turn_run.run_distribute_msg import build_queue2_booster_by_ip, ip_102

"""
现在是在单台机器模拟 实现  "两个机器轮流运行消息,并且同时只有一台机器在执行消息,同时只有一个消息被执行,不允许并发运行消息 " 这个需求,
实际上是动态自动获取当前机器ip,不需要 run_execute_msg_on_host101.py run_execute_msg_on_host102.py 两个重复的文件
"""

booster = build_queue2_booster_by_ip(ip_102)

if __name__ == '__main__':
    booster.consume()