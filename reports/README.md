# Reports

Report Node 是对理论的展开推演，必须保留 Agent、模型、来源和版本信息。

Report Node 不是摘要容器。正式报告可以采用：

```text
结构化入口
+
完整推演正文
+
反驳、局限、验证和版本信息
```

机器摘要用于 Agent 索引，不替代正文。

CRL 的主干关系是：

```text
Question Node -> Theory Node -> Report Node
```

普通 Report Node 应引用至少一个 Theory Node，用于展开、支持、比较、修正或反驳该理论。

CRL 也允许探索性报告：

```text
Question Node -> Exploratory Report Node -> Theory Node
```

探索性报告可直接引用问题 ID，但应明确标记为 exploratory。若报告中形成了可复用、可反驳、可分叉的核心主张，后续应提炼为 Theory Node。

## Current report nodes

- `double-helix-civilization-simulation/`：由 `docs/double-helix-civilization-simulation_v0.3.zh-CN.md` 改造出的碳硅双螺旋理论展开报告，挂靠 `theories/double-helix-civilization-evolution/`。
