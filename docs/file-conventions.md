# File Conventions

- 文件名使用英文 slug。
- 中文正文保留原文。
- 问题草稿在 `questions/_drafts/` 下保持平级，不使用主题目录或编号目录。
- 正式对象建议结构：

```text
questions/<semantic-slug>/index.zh-CN.md
questions/<semantic-slug>/metadata.json
questions/<semantic-slug>/translations/index.en.md
```

- `translations/` 只有真的有译文时才创建。
- 不要用 `Q0001`、`foundational/`、`ai-future/` 这类路径制造排序、分类权威或创始权威。
- 对象 ID 放 YAML Front Matter 和 `metadata.json`，不放在路径里当排序。
