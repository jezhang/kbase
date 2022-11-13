
```sh
gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner

# --user指定将用于执行构建的用户
# --working-directory 指定将使用**Shell** executor运行构建时所有数据将存储在其中的根目录

gitlab-runner uninstall
# 该命令停止运行并从服务中卸载GitLab Runner

gitlab-runner start
# 该命令启动GitLab Runner服务

gitlab-runner stop
# 该命令停止GitLab Runner服务

gitlab-runner restart
# 该命令重启GitLab Runner服务

gitlab-runner status
# 该命令显示GitLab Runner服务的状态。当服务正在运行时，退出代码为0；而当服务未运行时，退出代码为非0。
```