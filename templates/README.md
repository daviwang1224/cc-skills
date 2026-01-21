# 模板

本目录包含创建新技能和插件的模板文件。

## 📄 可用模板

### skill-template/
技能模板，包含：
- **SKILL.md**: 标准技能文件模板，包含必需的frontmatter和sections

### plugin-template/
插件模板，包含：
- **plugin.json**: 插件元数据配置模板

## 🚀 使用方式

### 创建新技能

1. 复制skill-template目录：
   ```bash
   cp -r templates/skill-template plugins/<plugin-name>/skills/<skill-name>
   ```

2. 编辑SKILL.md，填充内容：
   - 修改frontmatter（name, description, allowed-tools）
   - 填写核心能力
   - 编写详细流程
   - 添加参考资源（如需要）

3. 注册到marketplace.json

### 创建新插件

1. 创建插件目录结构：
   ```bash
   mkdir -p plugins/<plugin-name>/.claude-plugin
   ```

2. 复制并编辑plugin.json：
   ```bash
   cp templates/plugin-template/plugin.json plugins/<plugin-name>/.claude-plugin/
   ```

3. 编辑plugin.json填充插件信息

4. 注册到marketplace.json

## 📚 详细说明

查看 [CLAUDE.md](../CLAUDE.md) 获取完整的创建指南。
