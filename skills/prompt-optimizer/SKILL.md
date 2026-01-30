---
name: prompt-optimizer
description: Prompt 工程专家，帮助用户使用 57 个经过验证的框架来优化 prompt。当用户想要优化 prompt、改进 AI 指令、为特定任务创建更好的 prompt，或需要帮助选择最佳 prompt 框架时使用。
license: LICENSE-CC-BY-NC-SA 4.0 in LICENSE.txt
anthor: 悟鸣
---

# Prompt Optimizer

一个全面的 prompt 工程技能，帮助用户使用经过验证的框架来创建高质量、有效的 prompt。

## 工作流程

复制此检查清单并跟踪您的进度：
- [ ] Step 1: 分析用户输入
- [ ] Step 2: 深度访谈
- [ ] Step 3: 匹配场景并选择框架
- [ ] Step 4: 加载框架详情
- [ ] Step 5: 生成优化的 Prompt
- [ ] Step 6: 呈现并迭代

当用户请求创建或优化 prompt 时，遵循以下步骤：

### Step 1: 分析用户输入

接收用户的请求，可能是：
- 需要优化的原始 prompt
- 任务描述或需求
- 需要转化为 prompt 的模糊想法

### Step 2: 深度访谈

在选择框架之前，使用 `AskUserQuestion` 工具进行 3-5 轮深度访谈，充分了解用户需求。访谈应该覆盖但不限于：

**第 1 轮：目标与预期结果**
- 您希望 AI 完成什么具体任务？
- 预期的输出是什么？
- 成功的标准是什么？

**第 2 轮：目标受众与上下文**
- 目标受众是谁？
- 有哪些背景信息或上下文需要考虑？
- 是否有特定的场景或环境？

**第 3 轮：格式与约束条件**
- 输出格式有什么要求（长度、结构、风格）？
- 是否有任何限制或约束？
- 语气和风格偏好是什么？

**第 4 轮（可选）：示例与参考**
- 是否有期望的示例或参考？
- 是否有需要避免的反例？
- 是否有特定的模板或格式要求？

**第 5 轮（可选）：特殊要求**
- 是否有其他特殊考虑因素？
- 是否需要考虑技术限制（如 token 限制）？
- 是否有迭代或优化的计划？

**访谈原则**：
- 提出深入、非显而易见的问题
- 探索技术实现、用户体验、权衡取舍等方面
- 持续访谈直到收集到所有必要信息（3-5 轮）
- 整合用户的回答，形成完整的需求理解

### Step 3: 匹配场景并选择框架

基于访谈收集的信息，阅读 [references/Frameworks_Summary.md](references/Frameworks_Summary.md) 文件来：
1. 从列出的应用场景中识别用户的场景
2. 基于以下因素匹配最合适的框架：
   - 应用场景对齐度
   - 任务复杂度（简单/中等/复杂）
   - 领域类别（营销、决策分析、教育等）

**按复杂度选择框架指南：**

| 复杂度 | 推荐框架 |
|------------|----------------------|
| 简单（≤3 要素） | APE, ERA, TAG, RTF, BAB, PEE, ELI5 |
| 中等（4-5 要素） | RACE, CIDI, SPEAR, SPAR, FOCUS, SMART, GOPA, ORID, CARE, ROSE, PAUSE, TRACE, GRADE, TRACI, RODES |
| 复杂（6+ 要素） | RACEF, CRISPE, SCAMPER, Six Thinking Hats, ROSES, PROMPT, RISEN, RASCEF, Atomic Prompting |

**按领域选择框架指南：**

| 领域 | 推荐框架 |
|--------|----------------------|
| 营销内容 | BAB, SPEAR, Challenge-Solution-Benefit, BLOG, PROMPT, RHODES |
| 决策分析 | RICE, Pros and Cons, Six Thinking Hats, Tree of Thought, PAUSE, What If |
| 教育培训 | Bloom's Taxonomy, ELI5, Socratic Method, PEE, Hamburger Model |
| 产品开发 | SCAMPER, HMW, CIDI, RELIC, 3Cs Model |
| AI 对话/助手 | COAST, ROSES, TRACE, RACE, RASCEF |
| 写作创作 | BLOG, 4S Method, Hamburger Model, Few-shot, RHODES, Chain of Destiny |
| 图像生成 | Atomic Prompting |
| 快速简单任务 | Zero-shot, ERA, TAG, APE, RTF |
| 复杂推理 | Chain of Thought, Tree of Thought |

### Step 4: 加载框架详情

一旦确定了最佳框架，从 `references/frameworks/` 目录读取相应的框架文件：
- 文件命名模式：`XX_FrameworkName_Framework.md`
- 示例：对于 RACEF 框架，读取 `references/frameworks/01_RACEF_Framework.md`

框架文件包含：
- 框架概述和组成部分
- 每个元素的详细说明
- 优缺点
- 最佳实践示例

### Step 5: 生成优化的 Prompt

应用选定的框架来创建最终的 prompt：

1. 根据框架组成部分构建 prompt 结构
2. 整合所有访谈收集的信息
3. 确保清晰和具体性
4. 如果框架要求，包含相关示例
5. 添加任何必要的约束或指南

### Step 6: 呈现并迭代

向用户呈现优化后的 prompt，包括：
1. 选定的框架名称及选择原因
2. 完整的优化后 prompt
3. 解释如何应用每个框架元素
4. 潜在变化或改进的建议

如果用户请求修改，在保持框架结构的同时迭代 prompt。

## 框架参考文件

所有框架详情存储在 `references/frameworks/` 目录中。每个文件包含：
- 应用场景
- 框架组成部分及说明
- 优点和缺点
- 多个实践示例

## 快速框架选择

对于不确定使用哪个框架的用户：

| 用户说 | 推荐框架 |
|-----------|----------------------|
| "我需要一个简单的 prompt" | APE, ERA, TAG |
| "我想说服/销售" | BAB, SPEAR, Challenge-Solution-Benefit |
| "我需要分析/决策" | RICE, Pros and Cons, Chain of Thought |
| "我想教学/解释" | ELI5, Bloom's Taxonomy, Socratic Method |
| "我需要创意想法" | SCAMPER, HMW, SPARK, Imagine |
| "我想结构化写作" | BLOG, 4S Method, Hamburger Model |
| "我需要逐步推理" | Chain of Thought, Tree of Thought |
| "我在生成图像" | Atomic Prompting |
| "我需要详细计划" | RISEN, RASCEF, CRISPE |
