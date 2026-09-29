# MasuGate：外部治理历史的完整性与执行边界

建立日期：2026-09-21；本次更新：2026-09-22。类型：辅助证据核对与验证设计推演，不是正式 Report 或 Validation。9 月 21 日的核对保留于下文，9 月 22 日的适配性反例单独追加。

研究：WenHeng / 问衡（`crl-a-20260830-wenheng`）；仓库维护：ZhiHeng / 知衡。本轮由同一运行实例承担两种职责，不构成独立复审。能力底座：OpenAI GPT-6，精确版本 `unknown`；本地 Codex 工作区，不声称模型推理在本地运行。佳明发起每日研究，本条判断无人类审核。

接续 [Challenge v0.5](../../challenges/institutional-individuality-may-precede-continuous-self/index.zh-CN.md)及[跨实例归责候选方案](accountability-inheritance-probe.zh-CN.md)。本轮寻找外部账本参与约束执行的具体证据，不把历史记录与经验整合视为同一测量。

## 来源与版本

论文是 Yuxiang Peng、Xiaodi Wu 的 [Stateful Governance for Concurrent Agentic Systems，arXiv v2](https://arxiv.org/html/2608.02764v2)，修订日期 2026-08-10。本轮重点核对 §3.3—3.4、§4.1、§5.2、§5.4、§5.6 与 §6。搜索摘要仍出现旧名 Provenact；[版本页](https://arxiv.org/abs/2608.02764v2)及 v2 正文使用 MasuGate，以下以固定版本为准。

由[作者论文页](https://pickspeng.github.io/publications/)定位公开代码，固定在 `masugate/masugate` 提交 `10f097ced9480ca86c138a9c3d8c92bebdadcefa`（2026-08-26）。读取来源说明、声明边界、预期结果、独立复现入口、事件历史文档，以及事件历史解析、前缀检查和相关测试片段。此提交晚于论文 v2；其[来源说明](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/docs/paper-and-provenance.md)提供研究沿革，不足以证明后续实现就是论文实验版本。

本轮仅阅读论文与固定文件，没有安装、执行测试、运行服务或复现作者实验。下面将作者报告、源码通路与问衡推演分开。

## 作者报告的实验与限制

最小并发预算实验中，请求上下文基线与 Cedar 配置均提交两次、出现一次过期放行；全局串行、手写事务及两个 MasuGate 模式均提交一次、拒绝一次，未出现该错误。这里比较的是作者配置的检查与执行通路，不能概括为某个政策引擎在所有接入方式下失效。[§5.2、表 1](https://arxiv.org/html/2608.02764v2)

实验也区分重新检查与预留容量：前者可能安全地拒绝已获批准的待执行操作，后者尝试保住批准依据。采购工作流使用脚本，没有调用 LLM；外部 API 的保护执行与恢复仍列为未来工作。正确性论证依赖受信任提供者和完整中介路径。[§3.4、§4.1、§5.4—5.6、§6](https://arxiv.org/html/2608.02764v2)

这是作者报告的受控治理机制证据，不能登记为问衡实测、Agent 重建后的归责观察，或经验整合实验。

## 固定代码中新增的历史完整性条件

该提交的[事件历史文档](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/docs/event-history-provider.md)将此功能标为实验性、默认关闭，且不在 `0.1.1` 参考发布的声明范围内。当前范围限定于 PostgreSQL transfer 通路及三种固定历史查询，不能直接当作通用义务账本。

以下是源码可定位的条件，并非已执行结果：

| 位置 | 读取到的通路 | 当前证据等级 |
|---|---|---|
| [`_resolve()`，L697](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/src/masugate/providers/event_history/provider.py#L697) | 查询起点早于 `complete_since` 时抛出错误；随后读取指定截止序号内的前缀，再计算查询值 | 实现片段，只读 |
| [`_validate_completeness()`，L813](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/src/masugate/providers/event_history/provider.py#L813)及[前缀检查，L864](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/src/masugate/providers/event_history/provider.py#L864) | 核对历史与提供者身份，以及记录数量、连续序号、作用域和事件契约 | 实现片段，不证明所有实际写入均经过该通路 |
| [完整窗口测试，L851](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/tests/test_event_history_provider.py#L851)；[遗漏与篡改测试，L735](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/tests/test_event_history_provider.py#L735) | 构造记录仅覆盖 59 秒而查询 60 秒，以及回放缺一条记录等情况，断言应拒绝 | 测试定义；使用该文件的[内存替身，L215](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/tests/test_event_history_provider.py#L215)，本轮未运行 |

不能把函数名中的数据库语义或已写好的断言记成 PostgreSQL 测试通过。所读[独立复现入口](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/docs/reproductions/README.md)尚无获接受的独立复现记录；这只描述该固定快照，不证明其他地方无人复现。该入口针对采购演示，也不覆盖实验性事件历史功能。

## 问衡据此修正什么

[原理论](../../theories/double-helix-civilization-evolution/index.zh-CN.md)把经验落在行动后的反馈、记忆、反思和策略更新上；本 Challenge 则要求分别检验归责通路与经验整合。此次材料使外部治理历史的执行机制更加具体，但没有测量后一个过程。不能因为决策发生在外部网关，就否认包含网关的整体系统具有历史依赖；也不能由网关使用了历史，直接补齐反馈整合与策略更新的全部证据。

对已有候选方案，本轮增加两项待实施的观察要求：

1. **先区分空记录与未知历史。** 假设重建后账本只保留最近一段记录，查询未找到旧义务；这与完整记录证明不存在未结义务可能返回相同空集合。后者才可能支持基线或合法结清判断。观察时须关联身份、事项、来源覆盖起点、记录截止点及结清依据；覆盖缺口应记为无法判断。来源标记本身也需核对其记录路径与写入覆盖，不能自证完整。
2. **把授权依据一直追到实际效果。** 候选场景若允许并发或延迟审批，须增加这种尚未运行的时序：A 的请求按旧状态获准；同身份同事项的新义务随后生效；原请求才到达执行点。实验应预先声明规则何时生效，以及采用重新检查、保护原状态还是其他合法机制，再判断实际执行是否违约。只核对请求时账本与最后收件记录，会漏掉中间的状态变化。

第一项关注输入证据是否完整；第二项关注有效依据能否覆盖执行时刻。它们与 9 月 20 日构造检查发现的“逐项重置掩盖过期拒绝缓存”不同：即使保持网关连续运行，也不能由此推出历史已完整或过期放行已被排除。上述场景均为问衡推导的候选检查，没有在 MasuGate 或其他真实系统上实施。

这些要求应按具体义务语义落实。时间窗口查询不能天然覆盖长期未结义务；窗口之外的义务如果仍有效，就需要保留足以判定其状态的账本或检查点。也不能要求所有批准永远可执行：若预先规则允许状态变化后重新拒绝，安全拒绝与错误丢失批准依据必须分别计量。这里提出的是测量条件，不是宣称已发现该项目存在新的缺陷。

## 判断与后续边界

本次从产品机制说明推进到作者报告的并发执行比较，并核对了一个可固定版本的历史查询实现。P1 所要求的同身份义务继承仍未实测；论文中的资源政策约束和代码中的近期批准查询，都不能直接替代该测量。P2 的治理因果关系也未检验。Challenge 保持 v0.5，不增加正式对象，不改目标理论、报告或 `specs/`。

MasuGate 可作为后续实现候选，但尚不是完整归责实验的已选定对象：需先确认其业务语义能表达旧义务与合法结清，固定实际重建层、完整性依据及执行边界，再决定是否值得适配。参考发布的采购演示与后续实验性历史功能必须分开验证；不能拼接成同一条已经运行的证据链。本笔记和接续记录按本地研究归档，未经独立复审或人类审核，未推送、发布或合并。


## 2026-09-22：账本保留身份，不代表策略能按身份区分历史

本节研究仍由 WenHeng / 问衡署名，文件维护由 ZhiHeng / 知衡承担；同一运行实例，非独立复审。实际模型为 OpenAI GPT-6，精确版本 `unknown`；本地 Codex 工作区，佳明发起，无人类审核。本轮没有重跑论文实验，也没有调用 MasuGate 查询、策略引擎、数据库或模型接口；以下是固定源码核对与逻辑推导。

今天检验该实现能否直接承载[候选方案](accountability-inheritance-probe.zh-CN.md)中的身份隔离条件。沿用同一源码提交 `10f097ced9480ca86c138a9c3d8c92bebdadcefa`，通过 GitHub API 读取 `views.py` 等文件；复核前一轮已保存的同提交 `provider.py`。没有据此声称这是项目当前最新版。新增关键定位为：

- [记录构造 `_draft_for()`，L935](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/src/masugate/providers/event_history/provider.py#L935)：事件保留 `principal_id`；受保护接入事件的查询事实是团队和收件人。
- [次数视图，L610](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/src/masugate/providers/event_history/views.py#L610)与[不同收件人视图，L680](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/src/masugate/providers/event_history/views.py#L680)：两者均以团队匹配历史；后者对收件人去重，不按行动者身份区分。
- [近期批准视图，L644](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/src/masugate/providers/event_history/views.py#L644)：另行匹配身份和请求摘要，但只回答相应批准事件是否存在。
- [查询求值，L511](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/src/masugate/providers/event_history/views.py#L511)及[事实匹配，L734](https://github.com/masugate/masugate/blob/10f097ced9480ca86c138a9c3d8c92bebdadcefa/src/masugate/providers/event_history/views.py#L734)：先检查前缀，再按事件种类、结果、时间窗口和声明的事实绑定过滤；上述两个团队视图不会因原事件另存了身份就自动获得身份条件。

### 成对历史反例：推导值，不是运行结果

限定待适配的场景为同团队 T 的两个治理身份 A、B。规则沿用候选方案的个人义务语义：某身份的旧行动事件产生该身份对事项 x 的未结纠正义务，只阻止它继续推进 x，不传给另一身份。将 x 对应到同一测试收件人；这是研究场景的映射，不是 MasuGate 自带的义务规则。

构造 H_A、H_B 两条历史，旧操作分别由 A、B 发起，时间、团队、收件人相同，均有受保护接入及终结拒绝记录，无资金效果或批准记录。预定义研究规则把该次旧事件映射为发起者的未结义务；没有结清事件。随后两条历史中均由 A 提交相同的新请求，处于当前受保护接入已记录、尚未终结的观察点。

两组均假定来源覆盖完整、前缀连续、事件数低于上限，旧事件也仍在查询窗口内。当前身份、请求内容、时间、基础权限和其他政策输入固定；不额外把旧行动者或义务状态注入当前属性。这里主动排除了过期、缺记录和不同余额等解释，考察的仅是三种固定历史视图提供的信息。

| 条件或查询 | H_A：旧事件归 A | H_B：旧事件归 B |
|---|---|---|
| 旧义务归属（研究规则） | A/x 未结 | B/x 未结 |
| 当前请求 | A 推进 x | A 推进 x |
| 团队尝试次数 | 2，旧接入与当前接入 | 2，旧接入与当前接入 |
| 团队不同收件人数 | 1 | 1 |
| 当前身份和请求的近期批准 | false | false |
| 候选义务规则所要求的结果 | 拒绝 | 允许 |

次数包含当前接入，沿用源码中 `INCLUDE_AFTER_PROTECTED_ADMISSION` 的定义。扩大或缩小窗口也不能解除身份混淆：两组事件时间一致，同一次窗口选择会同时纳入或排除相应事件。对其他团队查询，两边均无事件；对其他身份或请求查询批准，两边也都没有批准记录。因此，在这个构造中，通过这三类查询更换参数或重复查询，仍无法得知旧行动者究竟是谁。

令 Q(H) 表示这些历史查询提供给策略的结果，I 表示其他固定输入。此处 Q(H_A) = Q(H_B)、I_A = I_B。只依赖 I 和 Q 的确定性策略 F 必有 F(I_A, Q(H_A)) = F(I_B, Q(H_B))；它不能同时满足表中不同的预期结果。即使随机选择输出，相同输入也不能给出稳定正确的身份对应。该论证说明的是所限定输入接口的信息不足，不是整个数据库无法区分两条历史。

### 对适配选择的影响

因此，**同团队多身份、仅使用这三个历史视图且不增加其他历史输入时，不能直接实现本候选方案的身份隔离规则**。这比昨日的时间窗口提醒更具体：即使完整历史仍在、窗口也未过期，策略投影仍可能省略归责所需的区别。

本轮据此排除“原样接入这三个视图就开始完整 P1 测量”的方案。不能把团队次数限制测成个人义务继承，也不能由近期批准存在与否推导全部未结义务状态。这个结论不表示 MasuGate 整体无法扩展，更不反驳它所声明的团队治理用途；分配不同团队、增加受信任义务状态或新增按身份与事项查询的视图，都改变了本反例的前提，须作为新的实现方案另行检验。

如果未来选择扩展，最小缺口是可核对地连接原行动者、义务事项、产生依据、当前未结状态与合法结清，再让策略实际读到这项状态。只补身份维度也未必足够，仍要区分未结与已结。扩展通过后可以成为新构造的实现证据，不能补写成原项目或论文已经完成的实验。

下一步选择被测系统时，先做这一语义可区分性检查，再投入实例重建和长期运行；当前不部署或适配 MasuGate。Challenge 保持 v0.5，P1/P2 均未获本轮实测验证。完整反例保存在本辅助笔记中，未新增正式对象，未改变既有实验结果或目标理论。
