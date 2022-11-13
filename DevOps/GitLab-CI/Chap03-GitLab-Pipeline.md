
# GitLab Runner运行流水线

在运行GitLab Pilepine之前，先做2个检查：

## 查看GitLab Runner 状态

```sh
$ gitlab-runner list
Runtime platform                                    arch=amd64 os=linux pid=3952118 revision=7178588d version=15.5.1
Listing configured runners                          ConfigFile=/home/user/.gitlab-runner/config.toml
remote runner                                       Executor=docker Token=1234567890abcd-GyBsU URL=http://git.xxx.com

$ sudo gitlab-runner verify
Running in system-mode.
Verifying runner... is alive                        runner=oApSkvyS
```

## .gitlab-ci.yml流水线语法检查

依次进入项目->CI/CD->CI Lint进行语法检查，

> 建议：在编辑完.gitlab-ci.yml文件后复制到到CI Lint工具中进行语法检查验证并修正。


```yml
stages:
    - build
    - deploy
  
  build:
    stage: build
    tags:
      - build
    only:
      - master
    script:
      - echo "mvn clean "
      - echo "mvn install"

  deploy:
    stage: deploy
    tags:
        - deploy
    only:
        - master
    script:
        - echo "hello deploy"
```

## Pipeline 语法1

### job

在每个项目中，使用名为.giltlab-ci.yml的YAML文件配置GitLab CI/CD管道。在文件中可以定义一个或多个作业（job）。每个作业必须具有唯一的名称（不能使用关键字），每个作业是独立执行的。作业定义了在约束条件下进行相关操作，**每个作业至少要包含一个script。**

```yml
job1:
  script: "execute-script-for-job1"

job2:
  script: "execute-script-for-job2"
```

这里在pipeline中定义了两个作业，每个作业运行不通的命令。命令可以是shell或脚本。

### script

每个作业至少要包含一个script。

```yml
job:
  script:
    - uname -a
    - bundle exec rspec
```

> 注意：有时，script命令将需要用单引号或双引号引起来。例如，包含冒号命令(:)需要加引号，以便被包裹的YAML解析器知道来解释整个事情作为一个字符串，而不是一个"键：值"对。

使用特殊字符时要小心:
`:`, `{`, `}`, `[`, `]`, `,`, `&`, `*`, `#`, `?`, `|`, `-`, `<`, `>`, `=`, `!`, `%`, `@`

### before_script

用于定义一个命令，该命令在每个作业之前运行。**必须是一个数组**。指定的script与主脚本中指定的任何脚本串联在一起，并在单个shell中一起执行。

before_script失败导致整个作业失败，其他作业将不再执行。作业失败不会影响after_script运行。

### after_script

用于定义将在每个作业（包括失败的作业）之后运行的命令。

这必须是一个数组。

指定的脚本在新的shel1中执行，与任何before_script或script脚本分开。

### stages

用于定义作业可以使用的阶段，并且是全局定义的。

同一阶段的作业并行运行，不同阶段按顺序执行。

```yml
stages:
  - build
  - test
  - codescan
  - deploy
```

### .pre&.post

.pre始终是整个管道的第一个运行阶段，.post始终是整个管道的最后一个运行阶段。用户定义的阶段都在两者之间运行。.pre和.post的顺序无法更改。如果管道仅包含.pre或.post阶段的作业，则不会创建管道。

![](http://picbed.ztm.me/202211131031120.png)

### stage

是按JOB定义的，并且依赖于全局定义的stages。它允许将作业分为不同的阶段，并且同一stage作业可以并行执行（取决于特定条件）

![](http://picbed.ztm.me/20221113103759.png)

可能遇到的问题：阶段并没有并行运行。
在这里我把这两个阶段在同一个runner运行了，所以需要修改runner每次运行的作业数量。默认是1，改为10.

修改/etc/gitlab-runner/config.toml 更改后自动加载无需重启

```sh
concurrent = 10
```

### variables

定义变量，pipeline变量、job变量。job变量优先级最大。


## Pipeline 语法2

tags/allow_failure/when/retry/timeout/parallel

### tags-指定runner

用于从允许运行该项目的所有Runner列表中选择特定的Runner，在Runner注册期间，您可以指定Runner的标签。

```yml
windows job:
  stage:
    - build
  tags:
    - windows
  script:
    - echo Hello, %USERNAME%!

osx job:
  stage:
    - build
  tags:
    - osx
  script:
    - echo "Hello, $USER!"
```

在runner里定义的tags

![](http://picbed.ztm.me/20221113104639.png)

### allow_failure-允许失败

allow_failure允许作业失败，默认值为false。启用后，如果作业失败，该作业将在用户界面中显示橙色警告。
但是，管道的逻辑流程将认为作业成功/通过，并且不会被阻塞。假设所有其他作业均成功，则该作业的阶段及其管道将显示相同的橙色警告。但是，关联的提交将被标记为"通过"，而不会发出警告。

```yml
unit-test:
    stage: test
    script:
        - echo "run unit test"
        - ech
        - sleep 3;
    allow_failure: true
```

![](http://picbed.ztm.me/20221113110229.png)

### when-控制作业运行

 - **on_success** 前面阶段中的所有作业都成功(或由于标记为allow_failure而被视为成功)时才执行作业，默认值。
 - **on_failure** 当前面阶段出现失败时执行。
 - **always** 总是执行作业。
 - **manual** 手动执行作业。
 - **delayed** 延迟执行作业。
 
 ![](http://picbed.ztm.me/20221113114128.png)

 ### retry-重试

 - 配置在失败的情况下重试作业的次数。
 - 当作业失败并配置了retry，将再次处理该作业，直到达到retry关键字指定的次数。
 - 如果retry设置为2，并且作业在第二次运行成功（第一次重试），则不会再次重试.retry值必须是一个正整数，**大于等于或0，但小于或等于2**（最多两次重试，总共运行3次）

 ![](http://picbed.ztm.me/20221113115206.png)

### retry-重试-精确匹配错误

默认情况下，在失败情况下重试作业。max：最大重试次数 when：重试失败的错误类型

 - always：在发生任何故障时重试（默认）
 - unknown_failure：当失败原因未知时。
 - script_failure：脚本失败时重试。
 - api_failure：API失败重试。
 - stuck_or_timeout_failure：作业卡住或超时时。
 - runner_system_failure：运行系统发生故障。
 - missing_dependency_failure：如果依赖丢失。
 - runner_unsupported：RunnerT受支持。
 - stale_schedule：无法执行延迟的作业。
 - job_execution_timeout：脚本超出了为作业设置的最大执行时间。
 - archived_failure：作业已存档且无法运行。
 - unmet_prerequisites：作业未能完成先决条件任务。
 - scheduler_failure：调度程序未能将作业分配给运行scheduler_failure。
 - data_integrity_failure：检测到结构完整性问题。

![](http://picbed.ztm.me/20221113121156.png)


### timeout-超时

超时包含作业超时、项目超时和Runner超时。作业级别的超时可以超过项目级别超时，但不能超过Runner特定的超时。

#### 作业超时

```yml
build:
  script: build.sh
  timeout: 3 hours 30 minutes

test:
  script: rspec
  timeout: 3h 30m
```


#### 项目超时

配置位置：项目->settings->CI/CD->General pipelines->Timeout(1h)

#### Runner超时

配置位置：Runner->Maximum job timeout

如果小于项目定义超时时间将具有优先权。此功能可用于通过设置大超时（例如一个星期）来防止Shared Runner被项目占用。未配置时，Runner将不会覆盖项目超时。

 - 示例1-运行程序超时大于项目超时
runner超时设置为24小时，项目的CI/CD超时设置为2小时。
该工作将在2小时后超时。
 - 示例2-未配置运行程序超时
runner不设置超时时间，项目的CI/CD超时设置为2小时。
该工作将在2小时后超时。
 - 示例3-运行程序超时小于项目超时
runner超时设置为30分钟，项目的CI/CD超时设置为2小时。
工作在30分钟后将超时

### parallel-并行作业

 - 配置要并行运行的作业实例数，此值必须大于或等于2并且小于或等于50。
 - 这将创建N个并行运行的同一作业实例，它们从job_name 1/N到job_nameN/N依次命名。

![](http://picbed.ztm.me/20221113123058.png)


## Pipeline 语法3

only/except/rules/workflow


### only&except-限制分支标签(outdated)

only和except用分支策略来限制jobs构建：
 - only定义哪些分支和标签的git项目将会被job执行。
 - except定义哪些分支和标签的git项目将不会被job执行。

```yml
job:
  # use regexp
  only:
    - /^issue-.*$/
  # use special keyword
  except:
    - branches
```

| Value                  | Description     | 
|------------------------|-----------------|
| branches               | 当管道的Git引用是分支时 |
| tags                   | 当管道的Git引用是标签时 |
| api                    | 当第二个管道API触发了管道时（不是触发器API） |
| external               | 使用除GitLab以外的CI服务时 |
| pipelines              | 对于多项目触发器，使用带有CI_JOB_TOKEN的API创建 |
| pushes                 | 管道由用户的git push触发 |
| schedules              | For scheduled pipelines |
| triggers               | 对于使用触发令牌创建的管道 |
| web                    | 对于使用GitLab UI中的"运行管道"按钮创建的管道（在项目的Pipelines下） |
| merge_requests         | 创建或更新合并请求时 |
| external_pull_requests | 在GitHub上创建或请求外部拉取请求时 |
| chat                   | 对于使用GitLab ChatOps命令创建的作业 |

![](http://picbed.ztm.me/20221113130046.png)

### rules-构建规则

 - rules允许按顺序评估单个规则，直到匹配并为作业动态提供属性。
 - rules不能与only/except组合使用。

可用的规则：
 - if (如果条件匹配)
 - changes (指定文件发生变化)
 - exists (指定文件存在)

#### rules-if-条件匹配

HOST: gitlab.cn
![](http://picbed.ztm.me/20221113134124.png)

HOST: gitlab.com
![](http://picbed.ztm.me/20221113133247.png)

HOST: gitlab.org
![](http://picbed.ztm.me/20221113133847.png)

#### rules-changes-文件变化

```yml
rules:
  - changes:
    - Dockerfile

```

#### rules-changes-文件存在



### workflow
