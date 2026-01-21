# Data Model Engineering Plugin

数据建模工程工具包，提供模型检查、设计和迁移能力。

## 📚 技能列表

### datamodel-checker

检查KMMOM数据模型设计文档的规范符合性和业务设计合理性。

**核心能力**:
- 验证7大检查维度（文档结构、命名规范、数据类型、引用完整性、继承关系、文档格式、业务设计）
- 跨文档引用验证（枚举、分类、单位、内置模型）
- 问题分级（严重错误❌ / 警告⚠️ / 提示ℹ️）
- 生成详细检查报告

**使用示例**:
```
请检查数据模型文档：03-development/datamodel-design/km-mom-tms-datamodel.md
```

## 📋 规范遵循

- ISA95工业数据模型标准
- KMMOM（KMM Object Model）设计规范
- 13种标准数据类型
- 5个内置抽象实体
- 10个标准接口

## 🔧 依赖

- Python 3.11+ （未来如需脚本支持）
- 无外部依赖

## 📖 更多信息

详见 [datamodel-checker 技能文档](skills/datamodel-checker/SKILL.md)
