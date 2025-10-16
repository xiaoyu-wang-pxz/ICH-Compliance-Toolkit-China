# ICH Compliance Toolkit (China) — v0.1
**Author / 作者**：Xiaoyu Wang（王晓宇）  
**Last updated / 更新日期**：2025-10-15

This open toolkit provides a minimal, ready-to-use workflow to audit and improve rights & source compliance for **digitised Intangible Cultural Heritage (ICH)** items in China, with a demonstration on **Douyin** videos.

本工具包提供一套最小可用的中文合规工具，帮助对**数字化非物质文化遗产**条目进行快速自检与规范化披露，并附抖音样本演示。

---

## Structure / 目录

- **templates/** 模板  
  - `N100_编码表模板.xlsx`：七要素下拉与自动统计的编码表  
  - `权利与来源声明_三档_中文.md`，`访问分级判定卡_红黄绿_中文.md`，`邻接权触发字段清单_中文.md`
- **code/** 代码  
  - `generate_summary.py`：读取编码表，输出缺漏率表与条形图
- **data/** 数据（示例）  
  - `抖音_抽样编码_N25.xlsx`（样本表）  
  - `summary_table_douyin_N25.xlsx`（缺漏率表）  
  - `summary_douyin_N25.png`（条形图）
- **docs/** 文档  
  - `Research_Note_模板_2-3页.docx`：研究备忘模板（中文）

---

## How to use / 使用方法

1. 在 `templates/N100_编码表模板.xlsx` 填写你的样本（建议 N≥100）。  
2. 运行 `code/generate_summary.py`，生成 `summary_table.xlsx` 与 `summary_preview.png`。  
3. 打开 `docs/Research_Note_模板_2-3页.docx`，将表格与图片粘贴进去，写出 2–3 页研究备忘录。  
4. 可将 `templates/*.md` 三份中文模板粘贴到网站/视频说明区，作为“最小合规声明”。

> **隐私/合规提示**：请仅使用公开页面的链接与元信息，勿上传含个人隐私或未经许可的原始影像。

---

## License / 许可
- **Code 代码**：MIT（见 `licenses/LICENSE_CODE_MIT.txt`）  
- **Documents & Templates 文档与模板**：CC BY 4.0（见 `licenses/LICENSE_DOCS_CC-BY-4.0.txt`）

---

## How to cite / 如何引用

**Toolkit / 工具包**  
> Wang, Xiaoyu (王晓宇). (2025). *ICH Compliance Toolkit (China), v0.1* [Data, Code, Templates].

**Research Note / 研究备忘录**（样本演示 N=25）  
> Wang, Xiaoyu (王晓宇). (2025). *Rights & Source Compliance in Douyin ICH Videos (China): A Rapid Scan (N=25).*

（发布到 OSF 或 GitHub/Zenodo 后，请在此补充 URL/DOI。）

---

## Keywords / 关键词
intangible cultural heritage; copyright; China; Douyin; compliance; metadata; governance
