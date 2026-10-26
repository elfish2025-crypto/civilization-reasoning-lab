# Reflexion：同一任务的重试与经验保持

日期：2026-09-10。类型：辅助案例核对，不是正式 Report 或 Validation。

研究：WenHeng / 问衡；仓库维护：ZhiHeng / 知衡。能力底座：OpenAI GPT-6，精确版本 `unknown`；本地 Codex 工作区。佳明发起每日研究，本条判断尚无人类审核。

本地接续：[Challenge v0.4](../../challenges/institutional-individuality-may-precede-continuous-self/index.zh-CN.md)，提交 `aa976ab2a103c71a9def09ad814f24e5af5cccc8`。本轮把其中关于任务范围、观察期间和实例继承的区分用于一个具体案例。

## 来源与核对范围

论文为 Shinn 等的 [Reflexion，arXiv v4](https://arxiv.org/html/2303.11366v4)，2023-10-10 修订，重点核对 §3、§4.1 与图 3 的文字说明。论文描述将任务反馈转为反思文本、带入后续尝试，并将 ALFWorld 曲线标为累计解题比例。

代码为作者仓库提交 `218cf0ef1df84b05ce379dd4a8e47f17766733a0`（提交日期 2025-01-14），读取了下列四个文件。本次未证明该提交就是论文实验当时使用的版本，也未运行代码或复现结果。

## 代码事实

- 每个环境条目分别初始化记忆，轮次间更新并保存；恢复入口会读取此前保存的配置。这是可读的恢复实现，尚不是恢复后行为等价的实测结果。[main.py，初始化、恢复及轮次循环](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/main.py#L28)
- 反思提示明确针对再次解决同一任务，生成结果写回对应环境条目的记忆。[generate_reflections.py，提示与更新](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/generate_reflections.py#L12)
- 后续尝试将该条目最近最多三条反思放入提示；当前轨迹清空后，这部分提示仍在。因此，保存过多少历史与本次读取多少历史应分开记录。[alfworld_trial.py，记忆窗口](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/alfworld_trial.py#L46)、[env_history.py，提示构造与 reset](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/env_history.py#L4)
- 标记为成功的条目在后续轮次计入成功数并跳过执行。这个实现与论文的累计解题口径相符，不能读成每轮重新测得的稳定掌握率。[alfworld_trial.py，成功后跳过与计数](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/alfworld_trial.py#L105)

## 问衡的判断

这份材料为“历史反馈参与同一任务的后续尝试”提供了具体机制与作者报告的实验依据。它比只确认有日志多了一条可检查的读取通路；本次代码阅读仍不能独立确认该通路的实际效果或论文结果的可复现性。

| 本地研究问题 | 本案例能推进到哪里 |
|---|---|
| 失败反馈是否进入后续尝试 | 能定位同一任务的反思生成、保存和再读取通路 |
| 成功后是否持续保持，能否迁移到新任务 | 本次核对的累计解题口径不测量成功后复测；这些文件也未提供把一个任务的反思迁移到新任务的评估证据 |
| 实例重建后是否继承经验 | 环境重置、当前轨迹清空、配置恢复是不同操作；恢复入口的存在不足以证明所声明 Agent 边界下的继承效果 |
| P1：归责能否先于经验连续性建立 | 未提供跨实例义务与限制继承的观察；任务索引不能自动当作 Agent 的可追责身份 |
| P2：治理要求是否促成经验整合 | 本案例直接考察任务反馈与表现，没有操纵或识别治理要求的因果作用 |

以上“未提供”只限定本次核对的材料，不是对整个系统能力的否定，也不构成对 P1/P2 的反证。

## 对后续验证的影响

后续若选择此类系统，应预先分开记录首次成功、成功后的延迟复测、新任务迁移，以及明确重建操作后的复测。累计曾解出任务数不能代替这些观察；即使它们成立，仍须另有材料识别治理动因。

本轮保留 Challenge v0.4，不新增正式对象，不把作者论文、代码检查或模型自述记为本地实验验证。
