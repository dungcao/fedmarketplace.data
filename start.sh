#!/bin/bash
rq worker -u redis://default:yO767yCXlIhLwIMWCbQtuRzFu2Y9qFL5@redis-10530.c252.ap-southeast-1-1.ec2.cloud.redislabs.com:10530 fmmlds7 &
rq worker -u redis://default:yO767yCXlIhLwIMWCbQtuRzFu2Y9qFL5@redis-10530.c252.ap-southeast-1-1.ec2.cloud.redislabs.com:10530 fmmlds8 &
rq worker -u redis://default:yO767yCXlIhLwIMWCbQtuRzFu2Y9qFL5@redis-10530.c252.ap-southeast-1-1.ec2.cloud.redislabs.com:10530 fmmlds9 &
