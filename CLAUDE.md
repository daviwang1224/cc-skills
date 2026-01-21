# 贡献指南

本文档描述如何为cc-skills仓库添加新的技能和插件。

## 📚 资源

**官方文档**:
- [Claude Code Plugins](https://docs.anthropic.com/en/docs/claude-code/plugins)
- [Agent Skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Best Practices](https://docs.anthropic.com/en/docs/claude-code/skills#best-practices)

## 🤔 何时创建新插件 vs 新技能

### 创建新技能（更常见）
当你的功能属于某个现有业务域时，在对应插件下创建新技能：
- datamodel-engineering → 添加数据建模相关技能
- ipd-project-management → 添加IPD项目管理相关技能
- architecture-design → 添加架构设计相关技能

### 创建新插件（较少）
当你的功能属于全新业务域，且预计有3+相关技能时：
- 例如：testing-automation、deployment-operations、security-audit

## ✨ 创建新技能的3个阶段

### 阶段1: 准备

1. **确定技能名称**
   - 使用kebab-case：`datamodel-checker`, `api-designer`
   - 优先动名词形式：`analyzing-contracts`, `generating-tests`
   - 避免模糊名称：`helper`, `utils`, `misc`

2. **确定所属插件**
   - 查看[README.md](README.md)的插件列表
   - 选择最相关的业务域

3. **编写触发描述**
   - 使用第三人称
   - 包含触发条件
   - 示例：`检查数据模型规范符合性和业务设计合理性。用于验证数据模型文档...当用户要求检查数据模型时使用。`

### 阶段2: 实施

1. **创建目录结构**
   ```bash
   mkdir -p plugins/<plugin-name>/skills/<skill-name>/references
   ```

2. **编写SKILL.md**（参考 [templates/skill-template/SKILL.md](templates/skill-template/SKILL.md)）
   ```markdown
   ---
   name: skill-name
   description: "第三人称描述，包含触发条件"
   allowed-tools: Read, Write, Grep, Glob
   ---

   # 技能标题

   ## 核心能力
   - 功能1
   - 功能2

   ## 使用方式
   用户指令示例

   ## 详细流程
   分步骤说明

   ## 参考资源
   [链接到references/中的文档]
   ```

3. **添加参考文档**（如需要）
   - 将详细内容放入 `references/` 目录
   - SKILL.md保持 < 500行
   - 采用渐进式披露

4. **添加脚本**（如需要）
   - Python脚本使用PEP 723内联依赖
   ```python
   # /// script
   # requires-python = ">=3.11"
   # dependencies = ["requests>=2.28"]
   # ///
   ```

### 阶段3: 注册

1. **更新marketplace.json**
   ```json
   {
     "plugins": [
       {
         "name": "plugin-name",
         "skills": [
           "./plugins/plugin-name/skills/skill-name/SKILL.md"
         ]
       }
     ]
   }
   ```

2. **更新插件README.md**
   - 在技能列表中添加新技能
   - 提供使用示例

3. **更新根README.md**
   - 更新技能数量统计
   - 更新路线图

## 📝 命名规范

| 对象 | 格式 | 示例 |
|------|------|------|
| 插件名 | kebab-case | `datamodel-engineering` |
| 技能名 | kebab-case | `datamodel-checker` |
| 技能文件 | 固定 | `SKILL.md` |
| 参考文档 | kebab-case.md | `isa95.md` |
| 脚本 | kebab-case.py | `validate_model.py` |

**避免使用**:
- camelCase, PascalCase, snake_case
- 保留字: `anthropic`, `claude`, `helper`, `utils`

## ✅ 质量检查清单

### SKILL.md必需elements

- [ ] YAML frontmatter包含name和description
- [ ] name使用kebab-case，≤64字符
- [ ] description是第三人称，包含触发条件
- [ ] allowed-tools准确列出所需工具
- [ ] 包含"核心能力"部分
- [ ] 包含"使用方式"部分
- [ ] 包含"详细流程"或"检查流程"部分
- [ ] 引用路径都指向references/中的文件
- [ ] 无硬编码绝对路径

### 描述质量

- [ ] 第三人称：`检查...` 而非 `我帮你检查...`
- [ ] 包含触发：`当用户要求检查数据模型时使用`
- [ ] 具体明确：`检查数据模型规范符合性` 而非 `数据模型工具`

### 文件组织

- [ ] SKILL.md < 500行（建议）
- [ ] 详细内容拆分到references/
- [ ] 引用深度≤1层（SKILL.md → reference.md，不要链式引用）
- [ ] 无冗余文件（不需要CHANGELOG, .gitignore等）

## 🔧 创建新插件

只有当你有**全新业务域**且**预计3+技能**时才创建新插件。

1. **创建目录结构**
   ```bash
   mkdir -p plugins/<plugin-name>/.claude-plugin
   mkdir -p plugins/<plugin-name>/skills
   ```

2. **创建plugin.json**
   ```json
   {
     "name": "plugin-name",
     "version": "1.0.0",
     "description": "插件描述",
     "author": {
       "name": "Your Name",
       "email": "your.email@example.com"
     },
     "homepage": "https://github.com/yourusername/cc-skills",
     "repository": "https://github.com/yourusername/cc-skills",
     "license": "MIT",
     "keywords": ["keyword1", "keyword2"]
   }
   ```

3. **创建插件README.md**
   - 插件简介
   - 技能列表
   - 使用示例

4. **注册到marketplace.json**
   ```json
   {
     "plugins": [
       {
         "name": "plugin-name",
         "description": "简短描述",
         "version": "1.0.0",
         "author": { "name": "Your Name" },
         "source": "./plugins/plugin-name",
         "category": "development",
         "skills": []
       }
     ]
   }
   ```

## 🧪 测试验证

### 本地测试

1. **加载市场**
   ```bash
   /plugin marketplace add ./cc-skills
   ```

2. **安装插件**
   ```bash
   /plugin install plugin-name
   ```

3. **触发测试**
   - 尝试触发技能的描述中提到的场景
   - 验证Claude能正确识别何时使用

4. **功能测试**
   - 执行完整工作流
   - 验证输出符合预期

## 📌 常见问题

### Q: 技能描述太长会怎样？
A: 描述会在每次可能触发时加载到上下文，建议控制在2-3句话，100-200字。

### Q: 可以在SKILL.md中直接写长篇参考文档吗？
A: 不建议。使用渐进式披露：SKILL.md保持精简，详细内容放references/，按需加载。

### Q: 何时使用scripts/目录？
A: 当有确定性、可重复的代码逻辑时（如PDF处理、数据解析），使用scripts/而非让Claude重复编写。

### Q: 如何避免技能触发冲突？
A: 编写具体的描述，明确"何时使用"和"何时不使用"。例如datamodel-checker明确说"当用户要求检查数据模型"。

## 📖 参考示例

- **基础示例**: [datamodel-checker](plugins/datamodel-engineering/skills/datamodel-checker/)
- **Anthropic官方**: [D:\5_repo\github\anthropics\skills](D:\5_repo\github\anthropics\skills)
- **Trail of Bits**: [D:\5_repo\github\skills](D:\5_repo\github\skills)

## 🎯 版本管理

使用语义化版本 MAJOR.MINOR.PATCH：
- **文件调整、修复** → PATCH (1.0.0 → 1.0.1)
- **新增技能** → MINOR (1.0.0 → 1.1.0)
- **重大重构** → MAJOR (1.0.0 → 2.0.0)

每次更新：
1. 更新plugin.json的version
2. 更新marketplace.json中对应插件的version
3. 如果是重大版本，考虑更新整个marketplace的metadata.version
