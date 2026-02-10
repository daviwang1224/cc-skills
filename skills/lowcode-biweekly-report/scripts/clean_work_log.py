#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""
低代码平台工作日志清洗脚本

功能：
1. 读取原始txt格式的工作日志
2. 清洗无效内容（农历、天气、金句、明日计划、本月计划等）
3. 按人员分类工作内容
4. 输出json格式的清洗后日志

使用方法：
    python clean_work_log.py input.txt output.json
    python clean_work_log.py input.txt output.json --verbose
"""

import re
import sys
import json
from pathlib import Path
from enum import Enum
from typing import Dict, List, Tuple

class State(Enum):
    """处理状态"""
    READING_CONTENT = "reading"  # 读取日期后的内容
    SKIPPING = "skipping"  # 跳过"每日金句"、"明日计划"、"本月计划"区域

class WorkLogCleaner:
    """工作日志清洗器"""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

        # 日期格式：yyyy-mm-dd
        self.date_pattern = r'^\d{4}-\d{2}-\d{2}'

        # 农历和天气描述（如：乙巳年 腊月十二 周五 小雨）
        self.lunar_weather_pattern = r'[甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥]年\s+\S+\s+周[一二三四五六日]\s+\S+'

        # []标签
        self.bracket_pattern = r'\[\]'

        # 触发跳过的关键词
        self.skip_triggers = ['每日金句', '明日计划', '本月计划', '月计划']

        # 姓名提取正则（支持全角和半角括号）
        self.name_pattern = r'[（(]([^）)]+)[）)]'

        # 低代码平台团队成员（用于过滤）
        self.team_members = {
            '王晴', '喻洁', '袁登', '尹进雄','方从哲',
            '施亚铭', '李正', '魏宪党', '方清', '廖沌金'
        }

    def log(self, message: str):
        """输出日志信息"""
        if self.verbose:
            print(f"[INFO] {message}")

    def is_date_line(self, line: str) -> bool:
        """判断是否为日期行"""
        return bool(re.match(self.date_pattern, line.strip()))

    def extract_date(self, line: str) -> str:
        """从行中提取日期"""
        match = re.match(self.date_pattern, line.strip())
        if match:
            return match.group(0)
        return ""

    def should_skip(self, line: str) -> bool:
        """判断是否应该进入跳过状态"""
        line = line.strip()
        for trigger in self.skip_triggers:
            if trigger in line:
                return True
        return False

    def clean_line(self, line: str) -> str:
        """清洗单行内容"""
        # 移除农历天气描述
        line = re.sub(self.lunar_weather_pattern, '', line)
        # 移除[]标签
        line = re.sub(self.bracket_pattern, '', line)
        return line.strip()

    def extract_names(self, line: str) -> List[str]:
        """
        提取括号中的姓名（支持全角和半角括号）
        返回姓名列表
        """
        matches = re.findall(self.name_pattern, line)

        if not matches:
            return []

        # 取最后一个匹配的括号内容
        names_str = matches[-1].strip()

        # 按顿号、逗号分隔姓名
        names = re.split(r'[、,，]', names_str)

        # 过滤出团队成员
        valid_names = []
        for name in names:
            name = name.strip()
            if name in self.team_members:
                valid_names.append(name)

        return valid_names

    def process_line(self, line: str, current_date: str,
                    details: Dict[str, Dict[str, List[str]]]):
        """
        处理单行日志

        Args:
            line: 当前行内容
            current_date: 当前日期
            details: 明细数据（按人员→日期→工作内容）
        """
        # 1. 清洗内容（移除农历天气、[]标签等）
        cleaned_line = self.clean_line(line)
        if not cleaned_line:
            return

        # 2. 提取姓名列表
        names = self.extract_names(cleaned_line)

        # 3. 根据姓名数量，决定如何处理
        if len(names) == 1:
            # 单个姓名 → 归入该人的明细区
            name = names[0]

            # 去掉姓名后缀（如"（王晴）"）
            content = re.sub(self.name_pattern, '', cleaned_line).strip()
            # 去掉末尾可能多余的分号
            content = content.rstrip('；;')

            if name not in details:
                details[name] = {}
            if current_date not in details[name]:
                details[name][current_date] = []
            details[name][current_date].append(content)
            self.log(f"归入明细区 [{name}][{current_date}]: {content[:50]}...")

        elif len(names) > 1:
            # 多个姓名 → 跳过，不提取
            self.log(f"跳过多人日志: {cleaned_line[:50]}...")

        else:
            # 没有姓名 → 跳过，不提取
            self.log(f"跳过无姓名内容: {cleaned_line[:50]}...")

    def clean_log(self, input_path: Path) -> Tuple[dict, dict]:
        """
        清洗工作日志

        返回：
            (cleaned_data, stats)
            cleaned_data: {summary, details}
            stats: 统计信息
        """
        self.log(f"开始读取文件: {input_path}")

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except UnicodeDecodeError:
            # 尝试GBK编码
            self.log("UTF-8解码失败，尝试GBK编码")
            with open(input_path, 'r', encoding='gbk') as f:
                lines = f.readlines()

        self.log(f"共读取 {len(lines)} 行")

        # 初始化数据结构
        details = {}  # {姓名: {日期: [工作内容列表]}}

        current_date = None
        state = State.SKIPPING  # 初始状态为跳过（直到遇到第一个日期）

        total_lines = len(lines)
        valid_lines = 0
        skipped_lines = 0

        for i, line in enumerate(lines):
            original_line = line
            line = line.strip()

            # 检查是否为日期行
            if self.is_date_line(line):
                current_date = self.extract_date(line)
                state = State.READING_CONTENT  # 遇到日期，进入读取状态
                self.log(f"发现日期: {current_date}，进入READING_CONTENT状态")
                continue

            # 如果还没有遇到日期，跳过
            if current_date is None:
                skipped_lines += 1
                continue

            # 检查是否应该进入跳过状态
            if state == State.READING_CONTENT and self.should_skip(line):
                state = State.SKIPPING
                self.log(f"遇到跳过触发词，进入SKIPPING状态: {line[:30]}...")
                skipped_lines += 1
                continue

            # 根据状态处理
            if state == State.READING_CONTENT:
                # 处理有效内容
                before_count = sum(len(logs) for dates in details.values() for logs in dates.values())

                self.process_line(line, current_date, details)

                after_count = sum(len(logs) for dates in details.values() for logs in dates.values())

                if after_count > before_count:
                    valid_lines += 1
                else:
                    skipped_lines += 1

            elif state == State.SKIPPING:
                skipped_lines += 1
                self.log(f"跳过内容: {line[:50]}...")

        # 统计汇总信息
        summary = self.calculate_summary(details)

        # 统计信息
        stats = {
            'total_lines': total_lines,
            'valid_lines': valid_lines,
            'skipped_lines': skipped_lines,
            'person_count': summary['person_count'],
            'work_days': summary['work_days'],
            'total_entries': sum(len(logs) for dates in details.values() for logs in dates.values())
        }

        self.log(f"清洗完成: {stats['person_count']} 个人员, {stats['work_days']} 个工作日, {stats['total_entries']} 条有效内容")

        cleaned_data = {
            "summary": summary,
            "details": details
        }

        return cleaned_data, stats

    def calculate_summary(self, details: Dict[str, Dict[str, List[str]]]) -> dict:
        """
        计算汇总信息

        Args:
            details: 明细数据

        Returns:
            汇总信息字典
        """
        # 统计日期范围
        all_dates = set()
        for person_dates in details.values():
            all_dates.update(person_dates.keys())

        period = ""
        if all_dates:
            sorted_dates = sorted(all_dates)
            start_date = sorted_dates[0]
            end_date = sorted_dates[-1]
            period = f"{start_date} - {end_date}"

        # 统计人数
        person_count = len(details)

        # 统计有效天数（有工作日志的天数）
        work_days = len(all_dates)

        return {
            "period": period,
            "person_count": person_count,
            "work_days": work_days
        }

    def convert_details_to_array(self, details: Dict[str, Dict[str, List[str]]]) -> Dict[str, List[str]]:
        """
        将 details 从嵌套字典格式转换为数组格式

        Args:
            details: 原始格式 {name: {date: [logs]}}

        Returns:
            数组格式 {name: ["date: log"]}
        """
        array_details = {}

        for name, dates in details.items():
            entries = []
            # 按日期排序
            for date in sorted(dates.keys(), reverse=True):  # 倒序，最新的在前
                logs = dates[date]
                # 合并同一天的多条日志
                combined_log = "；".join(logs)
                entries.append(f"{date}: {combined_log}")

            array_details[name] = entries

        return array_details

    def write_json(self, cleaned_data: dict, output_path: Path):
        """
        将清洗后的数据写入json文件

        Args:
            cleaned_data: 清洗后的数据
            output_path: 输出文件路径
        """
        self.log(f"开始写入文件: {output_path}")

        # 转换 details 格式为数组格式
        array_details = self.convert_details_to_array(cleaned_data['details'])

        # 构建输出数据
        output_data = {
            "summary": cleaned_data['summary'],
            "details": array_details
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        self.log(f"写入完成")


def main():
    """主函数"""
    # 解析命令行参数
    if len(sys.argv) < 3:
        print("使用方法: python clean_work_log.py <input.txt> <output.json> [--verbose]")
        print("\n示例:")
        print("  python clean_work_log.py 2025-01-工作日志.txt 2025-01_工作日志.json")
        print("  python clean_work_log.py input.txt output.json --verbose")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    verbose = '--verbose' in sys.argv or '-v' in sys.argv

    # 检查输入文件是否存在
    if not input_path.exists():
        print(f"错误: 输入文件不存在: {input_path}")
        sys.exit(1)

    # 创建清洗器
    cleaner = WorkLogCleaner(verbose=verbose)

    try:
        # 清洗日志
        cleaned_data, stats = cleaner.clean_log(input_path)

        # 写入json
        cleaner.write_json(cleaned_data, output_path)

        # 输出统计信息
        print("\n" + "="*50)
        print("清洗完成！")
        print("="*50)
        print(f"输入文件: {input_path}")
        print(f"输出文件: {output_path}")
        print(f"\n统计信息:")
        print(f"  总行数: {stats['total_lines']}")
        print(f"  有效行数: {stats['valid_lines']}")
        print(f"  跳过行数: {stats['skipped_lines']}")
        print(f"  人员数: {stats['person_count']}")
        print(f"  工作日数: {stats['work_days']}")
        print(f"  有效内容条数: {stats['total_entries']}")
        print("="*50)

    except Exception as e:
        print(f"\n错误: {e}")
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
