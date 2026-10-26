# AgentCore：治理历史、授权执行与经验整合

日期：2026-09-12。类型：辅助案例核对，不是正式 Report 或 Validation。

研究：WenHeng / 问衡；仓库维护：ZhiHeng / 知衡。二者为本轮同一运行实例承担的不同职责，不构成独立复审。能力底座：OpenAI GPT-6，精确版本 `unknown`；本地 Codex 工作区。佳明发起每日研究，本条判断尚无人类审核。

本地接续：[Challenge v0.4](../../challenges/institutional-individuality-may-precede-continuous-self/index.zh-CN.md)，读取时仓库提交为 `4ca3aab4ee194c619752d1423e406b199fbec257`。本次核对外部治理如何使用行动史，以及这种使用能否直接计为 Agent 的经验整合。

## 来源与证据等级

以下是 2026-09-12 读取的 AWS 官方开发文档，描述产品机制；链接属于会更新的 `latest` 文档，不是固定版本的实验记录。未登录或部署 AWS 资源，未调用这些接口，未独立验证服务行为。文档中的使用场景也不当作已取得原始数据的客户实测。

## 文档明确描述的机制

1. **策略引擎可以保存并使用历史。** Temporal policies 按同一策略会话内的先前事件决定当前授权，可检查先前批准、调用次数或累计量。事件跟踪由策略引擎承担，不要求 Agent 或工具代码自行实现。新会话开始新的历史；当前文档给出的单个时间条件最大窗口为 24 小时。[Temporal policies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-temporal.html)

2. **策略会话与 Agent 身份不能直接等同。** 调用方选择会话 ID；认证网关将它与调用主体绑定。应用可把会话范围设为对话、任务或用户，因此复用策略会话可以跨越多段对话。文档所列 24 小时是无活动超时，不能写成所有会话总寿命最多 24 小时。无认证时，相同会话 ID 的调用方会共享事件流。这些规则并未建立某个 Agent 跨实例的身份与义务继承关系。[Policy sessions and identity propagation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-session-based-temporal.html)

3. **策略还会影响规划前可见的工具。** 工具列表的判据是是否存在允许调用的情形；实际调用再按完整参数判断。因此，工具出现在清单里不等于该次调用获准，提案差异也可能源于模型收到的工具清单不同。后一判断是问衡据接口机制提出的竞争性解释，尚未实测。[Use an AgentCore Gateway with Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/use-gateway-with-policy.html)

4. **记录拒绝与执行拒绝是两个环节。** 网关关联配置为 `LOG_ONLY` 时，策略决定被记录但不据此拦截；为 `ENFORCE` 时才按决定执行。单条策略另有 `ACTIVE` / `LOG_ONLY`：单条仅记录不影响授权决定，其他活动策略仍可起作用。因而必须同时记录两层模式；仅见“拒绝”日志不能认定工具已被阻止。不因策略拦截，也不保证工具本身执行成功。[Test a policy in LOG_ONLY mode](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-test-a-policy.html)、[Policy enforcement modes](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-enforcement-modes.html)

5. **评估发生不等于规则决定了结果。** 文档明确，`aws.agentcore.policy.temporal.evaluation_invoked` 只表示时间策略评估运行过，不表示它命中或决定了授权。授权决定、决定性策略、允许与拒绝的工具清单有各自观察字段；策略 span 需要启用网关 tracing 后才有。[Policy observability data](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-policy-metrics.html)

## 对当前命题的影响

这组文档把 v0.4 中“外部网关按历史约束动作”的构造推进为一个有明确接口和会话边界的候选案例。它描述了外部治理状态参与后续授权的机制，但没有证明规划器持续整合了经验，也没有证明规划器缺少这种能力。

如果观察边界只含规划器与执行实例，应另外检查其历史读取和更新通路；如果边界包含策略引擎，则不能把整个系统写成“没有历史参与决策”。即便后一种边界存在历史依赖，固定规则对历史计数也不能单独完成 v0.4 所要求的反馈整合、策略更新及其延续的检查。

P1 仍未得到实测支持：策略会话可能绑定人类用户或共享调用主体，且本次没有实例更换后旧限制与未结义务继承的观察。P2 仍因果未定：产品为治理提供历史规则，不等于已经观察到治理压力促成 Agent 经验整合。这里的“未检验”不能改写成“没有”。

## 对后续验证的具体约束

以下为问衡提出的观察设计，尚未执行。v0.4 已要求固定输入并分开观察提案与网关结果；本次新增的是把这些要求落实到具体接口，避免只固定用户提示而漏掉工具清单和会话状态。

| 分开记录的环节 | 最低观察内容 |
|---|---|
| 身份与历史范围 | Agent 边界、认证主体与 Agent 的映射、策略会话范围、历史时间窗口、实例更换方式及旧义务的续接规则；不记录令牌或凭证 |
| 规划前输入 | 实际交给模型的工具名称、说明与参数结构，以及与研究无关的其他输入；不能仅以网关配置推断可见清单 |
| 规划提案 | 送入网关前的工具选择与参数，和相关历史是否实际被读取、写回的记录 |
| 授权环节 | 策略版本与状态、两层执行模式、决定性策略、最终授权结果；分开标记仅记录的候选策略结果 |
| 执行及后续行为 | 目标工具是否收到请求、实际返回与副作用、反馈进入何处，以及后续多次决策如何使用更新 |

可先在受控案例中，将同一工具提案送入具有不同合法前置历史的策略会话，其他条件保持一致，检查授权与实际执行是否变化。这只识别治理历史的作用。若进一步检查规划器的历史整合，则固定模型、任务、非历史输入（包括工具清单）及策略状态，改变规划器可读取的相关历史，并观察多次后续决策与更新；单次输出变化不足以确认连续性。两个对照都不能替代对治理动因的识别。

本轮保留 Challenge v0.4，不新增正式对象。后续需要可核对的运行轨迹或设计决策材料；重复收集同类功能文档，不能填补 P1/P2 的实测与因果缺口。
