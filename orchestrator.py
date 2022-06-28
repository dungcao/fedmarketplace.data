from redis import Redis
from rq import Queue
import subprocess
from Orchestration.jobs import start_client,remove_all_container

r = Redis(host='redis-10530.c252.ap-southeast-1-1.ec2.cloud.redislabs.com', port='10530', password='yO767yCXlIhLwIMWCbQtuRzFu2Y9qFL5')
fed_server = "13.250.107.136:8080"
run_th = "1"
for i in range(1, 11):
    client = "client{}.json".format(i)
    data = "fraudTrain_processed_SMOTE_{}.csv".format(i)
    print(client)
    print(data)
    q = Queue("fmmlds{}".format(i), connection=r)

    q.enqueue(f=start_client, args=(fed_server, client, data, run_th))

    # q.enqueue(f=remove_all_container)