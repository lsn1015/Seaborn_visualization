
# 餐饮运营数据分析项目
# Restaurant Operations Data Analysis Project

本项目使用经典 **tips** 数据集，对餐厅顾客消费行为和小费模式进行数据分析。  
This project uses the classic **tips** dataset to analyze customer spending behavior and tipping patterns in a restaurant setting.

通过可视化和统计分析，将数据洞察转化为餐厅运营策略，帮助管理者做出科学决策。  
Using visualization and statistical analysis, insights are translated into actionable restaurant operations strategies, enabling data-driven decision-making.

---

## 项目目标
## Project Purpose

本项目旨在通过数据分析回答以下业务问题：  
The project aims to address the following business questions:

- 不同性别顾客的消费模式有何差异？  
  How do spending patterns vary by customer gender?  
- 用餐时间对消费和小费有何影响？  
  How does meal time affect spending and tipping behavior?  
- 一周内高峰营业时间集中在哪些日子？  
  Which days of the week have peak business activity?  
- 数据洞察如何优化员工安排和营销策略？  
  How can data insights optimize staffing and marketing strategies?

---

## 项目结构
## Project Structure

```

project/
├── data/
│   └── tips.csv
├── src/
│   └── analysis.py        # 可视化与统计分析脚本 / Visualization and analysis script
├── output/
│   └── restaurant_analysis_final.csv
├── README.md
└── requirements.txt

````

---

## 工具与技术
## Tools & Technologies

- **Python**  
- **Pandas** 数据处理 / Data processing  
- **Seaborn** 统计可视化 / Statistical visualization  
- **Matplotlib** 绘图支持 / Plotting support  

安装依赖 / Install dependencies：

```bash
pip install -r requirements.txt
````

---

## 分析方法

## Analytical Approach

通过 Seaborn 可视化图表分析以下业务指标：
The analysis uses Seaborn visualizations to examine the following business metrics:

### 1. 每日消费模式

### 1. Spending Patterns Across Days

* 箱线图对比不同工作日的总账单和人均账单
  Boxplots comparing total and per-person bills across weekdays
* 识别高峰营业日（周五、周六）
  Identify peak business days (Friday and Saturday)

### 2. 性别差异

### 2. Gender-Based Behavior

* 性别分布计数图
  Countplots for gender distribution
* 箱线图比较男女顾客消费水平
  Boxplots comparing spending levels between male and female customers

### 3. 用餐时间分析

### 3. Meal Time Analysis

* 小提琴图观察午餐与晚餐的消费差异
  Violin plots to observe spending differences between Lunch and Dinner
* 散点图分析用餐时间对账单和小费的影响
  Scatterplots analyzing bill–tip relationship by time of day

### 4. 小费模式

### 4. Tipping Patterns

* 散点图展示总账单与小费关系
  Scatterplots showing correlation between total bill and tip
* 条形散点图显示不同性别/日期/时间的小费分布
  Stripplots to observe tipping patterns across gender/day/time

### 5. 数据处理与特征选择

### 5. Data Processing & Feature Selection

* 创建 `per_person_bill` 特征
  Create `per_person_bill` feature
* 删除 `smoker` 特征（分析价值低）
  Remove `smoker` feature (low analytical value)
* 保存清理后的数据集用于后续决策分析
  Save cleaned dataset for downstream decision-making

---

## 主要洞察

## Key Insights

基于数据分析得出的运营洞察 / Insights derived from data analysis:

### 顾客行为

### Customer Behavior

* 男性顾客平均消费更高，高额交易比例较高
  Male customers have higher average spending and more high-value transactions
* 周六小费最活跃，其次是周日
  Saturday shows the highest tipping activity, followed by Sunday

### 运营模式

### Operational Patterns

* 晚餐消费波动大，总账单偏高
  Dinner exhibits higher spending variation and overall higher bills
* 周五和周六晚餐为高峰营业时段
  Peak business occurs on Friday and Saturday evenings

### 小费模式

### Tipping Insights

* 小费主要集中在 0–4 美元
  Tips are mostly in the 0–4 USD range
* 高账单顾客通常支付更高小费
  Higher total bills are correlated with higher tips

---

## 商业建议

## Business Recommendations

基于数据洞察提供以下运营优化建议 / Recommendations based on data insights:

* **周五和周六晚餐**增加员工和服务能力
  Increase staffing and service capacity during Friday and Saturday dinners
* **午餐时段**推出促销套餐以提升客流
  Promote meal deals during lunch hours to boost traffic
* 针对 **女性新顾客** 和 **高消费男性顾客** 制定营销策略
  Target marketing strategies toward new female customers and high-spending male customers
* 晚餐时段确保服务质量以维持小费水平
  Maintain high service quality during dinner to sustain tipping behavior

---

## 输出数据

## Output

生成清理后的数据集，用于后续分析 / Produces a cleaned dataset for further analysis:

```
output/restaurant_analysis_final.csv
```

保留有价值特征，删除无关数据，方便业务分析
Keeps relevant features and removes unnecessary data for easier operational analysis

---

## 注意事项

## Notes

这是一个 **数据驱动商业分析练习项目**，主要用于：
This is a data-driven business analysis practice project, mainly for:

* 分析顾客消费行为与模式 / Analyzing customer spending behavior
* 从数据中提取运营洞察 / Extracting operational insights from data
* 基于数据提出业务优化策略 / Formulating business recommendations based on data
