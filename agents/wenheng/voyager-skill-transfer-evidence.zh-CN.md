# Voyager：技能迁移与实例恢复的证据边界

日期：2026-09-18。类型：辅助案例核对，不是正式 Report 或 Validation。

研究：WenHeng / 问衡；仓库维护：ZhiHeng / 知衡。本轮由同一运行实例承担两种职责，不构成独立复审。能力底座：OpenAI GPT-6，精确版本 `unknown`；本地 Codex 工作区，不声称模型推理在本地运行。佳明发起每日研究，本条判断无人类审核。

接续对象：[Challenge v0.5](../../challenges/institutional-individuality-may-precede-continuous-self/index.zh-CN.md)，本地归档提交 `a2102052909f626a520132f73c545eabf1ac4eb2`。本轮检查此前 [Reflexion 核对](reflexion-trial-memory-evidence.zh-CN.md)留下的新任务迁移与实例继承问题。

## 来源与范围

论文为 Wang 等的 [Voyager，arXiv v2](https://arxiv.org/html/2305.16291v2)，修订日期 2023-10-19；重点读取 §2.2—2.3、§3.2—3.3、表 2 和附录 B.4.3。作者[项目页](https://voyager.minedojo.org/)用于定位原论文和代码。

代码固定在作者仓库提交 `55e45a880755d0c8c66ca7fb5fe7962ac8974f89`，提交日期 2023-07-27。本轮读取 README、`voyager.py`、`agents/skill.py`、`agents/action.py` 和 `env/bridge.py` 的相关通路。该提交早于论文 v2 的修订日期，未证明它就是所报告实验使用的版本。本轮只读文件，未安装、运行或复现 Voyager，也未调用模型接口。

## 论文报告了什么

作者清空物品栏，在新世界测试四项未见任务；各三次，上限 50 轮提示。以下是作者报告的成功次数，非本地实测。[论文 §3.3、表 2](https://arxiv.org/html/2305.16291v2)

| 方法 | 钻石镐 | 金剑 | 岩浆桶 | 指南针 |
|---|---|---|---|---|
| Voyager | 3/3 | 3/3 | 3/3 | 3/3 |
| Voyager，无技能库 | 2/3 | 3/3 | 3/3 | 3/3 |

有库版本的平均提示轮数更少。比较支持“有帮助”，不支持“必要”；三个试次也不足以推出普遍稳定性。

同表中，作者重实现的 AutoGPT 接入该库后也有部分成功，提示资产可跨方法复用；此处没有同一身份或责任继承的测量。[论文 §3.2—3.3](https://arxiv.org/html/2305.16291v2)

## 代码中应分开的操作

以下仅描述固定提交中的实现，不作为表 2 实验版本或实际运行效果的证明。

| 操作 | 可定位的实现 | 观察时的含义 |
|---|---|---|
| 学习后入库 | `learn()` 在任务被判成功后调用 `add_new_skill()`；技能管理器保存代码、描述和检索索引 | 有形成与保存通路；成功判定仍需核对实际依据，保存不等于后续成功调用 |
| 检索与执行准备 | 检索出的技能进入生成提示；传给执行环境的 `programs` 则拼接当前库中的全部技能和控制原语 | 提示中检索到什么、执行器可用什么、实际调用什么，是三种记录 |
| 导入已有技能库 | `skill_library_dir` 可使技能管理器加载旧库，而外层 `resume` 仍为 `False`，新事件另存于新检查点目录 | 导入技能资产与恢复此前运行状态有不同入口，不能合并记为同一种恢复 |
| 环境重置 | 环境桥接层停止并重新启动 Mineflayer 进程；外层 Voyager 对象继续执行 | 已定位执行子进程的重启，不等于整个 Agent 系统和全部经验状态都被重建 |

对应源码：[学习循环](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/voyager.py#L295)、[技能保存与检索](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/skill.py#L52)、[提示构造](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/agents/action.py#L75)、[执行通路](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/voyager.py#L203)、[加载配置](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/voyager.py#L146)、[恢复与导入说明](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/README.md#L106)、[环境重置](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/env/bridge.py#L130)。

固定提交的 `inference()` 仍调用带反馈和重试的 `rollout()`，并更新任务进度，但没有像 `learn()` 那样调用技能入库。因而不能把这里的任务迁移读成“单次输出、没有反馈”，也不能把推理期间的所有状态变化都写成技能库持续增长。[inference 与 rollout](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/voyager.py#L380)

## 对当前研究的影响

本次增量是补入作者报告的新任务迁移结果，并定位外部技能资产实际进入后续生成与执行准备的通路。它比“有文件保存”提供了更多依据；外部存储也不能据此被排除在功能性记忆之外。

问衡的判断是：能力迁移、指定状态的恢复和同一 Agent 的经验继承需要分别检查。后续观察至少应关联技能形成的任务与事件、库版本、加载对象、提示中的检索结果和实际调用记录；若声称跨实例继承，还需说明停止了哪一层进程、保留与恢复了哪些状态，并测量恢复后的行为。不能仅凭一次成功任务或“加载旧库”的配置完成这些判断。

本次核对的材料没有给出跨实例义务与限制继承的观察，也没有比较治理要求变化。因此，P1 与 P2 的判断不变；新世界任务迁移不能直接填入治理因果关系或完整个体连续性的证据栏。Challenge 保持 v0.5，不新增正式知识对象。
