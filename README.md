# Personal Claude Code Skills

个人自定义Claude技能集合，涵盖数据建模、项目管理、架构设计等领域。

## 📦 插件列表

| 插件名称 | 描述 | 技能数量 | 类别 |
|---------|------|---------|------|
| [datamodel-engineering](plugins/datamodel-engineering/) | 数据建模工程工具包 | 1 | data |

**总计**: 1个插件, 1个技能 (目标50+)

## 🚀 安装方式

### 方法1: 添加本地市场（推荐）

在cc-skills的**父目录**中运行：
```bash
/plugin marketplace add ./cc-skills
```

### 方法2: 安装特定插件

```bash
/plugin install datamodel-engineering@cc-skills
```

### 方法3: 在Claude Code中浏览

```bash
/plugin menu
```

## 📚 技能详情

### 数据建模 (datamodel-engineering)

- **datamodel-checker**: 检查数据模型规范符合性和业务设计合理性
  - 验证7大检查维度（文档结构、命名规范、数据类型、引用完整性、继承关系、文档格式、业务设计）
  - 跨文档引用验证（枚举、分类、单位、内置模型）
  - 问题分级（严重错误❌ / 警告⚠️ / 提示ℹ️）
  - 生成详细检查报告

## 📚 文档

### 目录规划
- **[目录结构规范](docs/directory-structure-spec.md)**：cc-skills 的目录组织规范和命名约定
- **[具体目录规划](docs/directory-plan.md)**：基于 slash-command-kit 的 30 个 commands 的具体目录规划

### 贡献指南
- **[贡献指南](CLAUDE.md)**：如何添加新技能和插件

## 🛠️ 开发指南

### 添加新技能

1. 确定所属插件或创建新插件
2. 在 `plugins/<plugin-name>/skills/` 下创建技能目录
3. 编写 [SKILL.md](templates/skill-template/SKILL.md)（参考模板）
4. 更新 [marketplace.json](.claude-plugin/marketplace.json)
5. 更新插件README.md

详细步骤查看 [CLAUDE.md](CLAUDE.md)

## 📂 目录组织规范

### 仓库结构

```
cc-skills/
├── .claude-plugin/
│   └── marketplace.json
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md
│       ├── references/
│       ├── scripts/
│       ├── examples/
│       ├── templates/
│       └── assets/
├── template/
│   └── SKILL.md
├── docs/
├── README.md
└── CLAUDE.md
```

### 目录说明

**仓库级别**
- `.claude-plugin/` - 市场配置目录
- `skills/` - 所有技能的根目录
- `template/` - 技能模板目录
- `docs/` - 文档目录（可选）



## 📄 许可证

MIT License
