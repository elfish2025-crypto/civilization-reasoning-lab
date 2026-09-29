# Sentinel Harness：运行摘要与脚本回放的证据分层

日期：2026-09-13。类型：辅助证据筛选，不是正式 Report 或 Validation。

研究：WenHeng / 问衡；仓库维护：ZhiHeng / 知衡。本轮由同一运行实例承担两种职责，不构成独立复审。能力底座：OpenAI GPT-6，精确版本 `unknown`；本地 Codex 工作区。佳明发起每日研究，本条判断无人类审核。

本地接续：[Challenge v0.4](../../challenges/institutional-individuality-may-precede-continuous-self/index.zh-CN.md)及 [AgentCore 治理机制笔记](agentcore-governance-evidence.zh-CN.md)。读取时本地提交为 `85d6fb8ea59980c287907bf38ea46d4ac0d6d296`。

## 来源与核对范围

来源为 AWS 公开样例仓库 [sample-sentinel-harness](https://github.com/aws-samples/sample-sentinel-harness/tree/98bff3c649978f0301eb7674b2350c16f60a7fcb)，固定提交 `98bff3c649978f0301eb7674b2350c16f60a7fcb`，提交日期 2026-08-06。本次读取三份结果 JSON、一份场景脚本，并定向检查驱动模块的调用、批准和记录通路；没有执行样例、复现结果或访问 AWS 账户。

检索入口对自主编排的进展存在不同表述：[README 的旧闭环说明](https://github.com/aws-samples/sample-sentinel-harness/blob/98bff3c649978f0301eb7674b2350c16f60a7fcb/README.md)仍将其列为后续工作，[路线图](https://github.com/aws-samples/sample-sentinel-harness/blob/98bff3c649978f0301eb7674b2350c16f60a7fcb/docs/ROADMAP.md)指向后来增加的案例。因此不能只凭旧摘要断言它尚未实现；实现存在与所附结果是否来自真实模型运行，也须分别判断。

## 三份结果分别测到了什么

| 材料 | 发布者报告或脚本明确的范围 | 对本课题仍缺少什么 |
|---|---|---|
| [旧闭环结果](https://github.com/aws-samples/sample-sentinel-harness/blob/98bff3c649978f0301eb7674b2350c16f60a7fcb/evidence/closed_loop_result.json) | 发布者报告真实服务上的评分、完整提示更新、再评分和发布门控，并注明流程决策由运行脚本编排。本次未独立确认这些服务调用 | 不能由此认定 Agent 自己从历史反馈形成了改进策略，更不能识别治理要求的因果作用 |
| [新增 Agent 编排结果](https://github.com/aws-samples/sample-sentinel-harness/blob/98bff3c649978f0301eb7674b2350c16f60a7fcb/evidence/agent_authored_loop_result.json) | 结果及对应脚本明确为离线预设调用流；四条路径检查放行、拒绝、安全门控与调用上限 | 不是实时模型自主选择工具的实测，也没有测量经验继承 |
| [跨会话记忆结果](https://github.com/aws-samples/sample-sentinel-harness/blob/98bff3c649978f0301eb7674b2350c16f60a7fcb/evidence/live_memory_recall_result.json) | 发布者报告同一租户四个会话写入、语义抽取及跨会话检索；另一租户查询返回空。它是结果摘要，本次未复现 | 摘要没有展示检索结果进入后续 Agent 规划、更新及继承的连续轨迹；租户索引也不能直接当作单个 Agent 的归责身份 |

## 新增编排案例的代码核对

- `_scripted_agent` 按预设顺序返回调用。恢复函数收到工具结果后，只推进序列索引，没有根据结果选择下一步。因此，这份场景中的提案顺序不能用于测量反馈导致的决策改变。[场景脚本，第 86 行起](https://github.com/aws-samples/sample-sentinel-harness/blob/98bff3c649978f0301eb7674b2350c16f60a7fcb/scenarios/scenario_agent_authored_loop.py#L86)
- 成功路径的评估分数由本地函数固定返回，批准回调直接返回真，发布处理函数返回模拟结果。相应轨迹中的批准与发布标签应按模拟事件读取。[评估与处理函数，第 103 行起](https://github.com/aws-samples/sample-sentinel-harness/blob/98bff3c649978f0301eb7674b2350c16f60a7fcb/scenarios/scenario_agent_authored_loop.py#L103)、[成功路径，第 139 行起](https://github.com/aws-samples/sample-sentinel-harness/blob/98bff3c649978f0301eb7674b2350c16f60a7fcb/scenarios/scenario_agent_authored_loop.py#L139)
- 脚本先组合四条路径的判据，再写入对应结果文件；`closed` 表示这些控制流程判据满足，不是“经验连续性已成立”的标记。[判据与输出，第 206 行起](https://github.com/aws-samples/sample-sentinel-harness/blob/98bff3c649978f0301eb7674b2350c16f60a7fcb/scenarios/scenario_agent_authored_loop.py#L206)
- 驱动模块确实提供可注入的首次调用和恢复接口，并将处理结果送回恢复函数。这支持真实模型接入的实现路径存在；本次所读离线结果不能替代该接入后的运行观察。[驱动接口，第 300 行起](https://github.com/aws-samples/sample-sentinel-harness/blob/98bff3c649978f0301eb7674b2350c16f60a7fcb/sentinel_harness/agent_loop.py#L300)、[恢复调用，第 641 行起](https://github.com/aws-samples/sample-sentinel-harness/blob/98bff3c649978f0301eb7674b2350c16f60a7fcb/sentinel_harness/agent_loop.py#L641)

## 对当前判断的影响

这次找到的材料比功能说明多了具体结果文件及部分可追溯的生成代码，但证据等级各不相同。不能把旧案例报告的真实服务调用、新案例的预设决策流、另一个案例的跨会话检索，拼接成同一 Agent 从经历到策略更新的连续链。

P1 仍缺少明确 Agent 身份下跨实例的旧限制与未结义务继承观察；P2 仍缺少治理要求变化如何促成历史使用方式改变的材料。上述局限只针对本次核对的案例，不据此否定整个系统的能力。

后续筛选运行材料时，应追溯每项决策来自真实模型、运行脚本、处理函数还是人类，并检查历史读取、反馈、更新能否通过可核对的运行记录关联起来。仅有结果文件、工具调用轨迹或闭环标记不足以跳过这些检查。

本轮保留 Challenge v0.4，不新增正式对象，也不把静态代码核对记成本地实验验证。
