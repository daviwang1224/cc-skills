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

## 🛠️ 开发指南

### 添加新技能

1. 确定所属插件或创建新插件
2. 在 `plugins/<plugin-name>/skills/` 下创建技能目录
3. 编写 [SKILL.md](templates/skill-template/SKILL.md)（参考模板）
4. 更新 [marketplace.json](.claude-plugin/marketplace.json)
5. 更新插件README.md

详细步骤查看 [CLAUDE.md](CLAUDE.md)

## 📂 仓库结构

```
cc-skills/
├── .claude-plugin/           # 市场配置
│   └── marketplace.json
├── plugins/                  # 插件目录
│   └── datamodel-engineering/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── skills/
│       │   └── datamodel-checker/
│       └── README.md
├── templates/                # 技能和插件模板
├── docs/                     # 文档
├── README.md                 # 本文件
└── CLAUDE.md                 # 贡献指南
```

## 🎯 路线图

### 近期计划
- ✅ datamodel-engineering 插件（1个技能）
- ⏳ 添加 datamodel-designer 技能
- ⏳ 添加 datamodel-migrator 技能

### 中期规划
- ⏳ ipd-project-management 插件（3个技能）
- ⏳ architecture-design 插件（3个技能）
- ⏳ documentation-toolkit 插件（3个技能）

### 长期目标
- 🎯 达到 50+ 技能
- 🎯 覆盖 5-8 个业务域

## 📄 许可证

MIT License
