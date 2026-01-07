# Student Performance Analysis

## Project Overview
This project analyzes student academic performance using Python.
The objective is to understand how study hours and subject-wise performance
affect student scores through data analysis and visualization.

The project demonstrates a complete data analysis pipeline including
data loading, cleaning, analysis, visualization, and reporting.

---

## Objectives
- Analyze student scores using real data
- Compare average performance across subjects
- Study the relationship between study hours and scores
- Visualize results using multiple chart types
- Generate meaningful academic insights

---

## Project Structure
```
student-performance-analysis/
│
├── README.md
├── main.py
├── requirements.txt
│
├── data/
│   └── student_performance.csv
│
├── visualizations/
│   ├── avg_score_subject.png
│   └── study_hours_vs_score.png
│
└── report/
    └── analysis_report.pdf
```

---

## Dataset Description
- **student_performance.csv**
  - Student_ID
  - Subject
  - Study_Hours
  - Attendance_Percentage
  - Score

---

## Tools and Technologies
- Python
- Pandas
- Matplotlib

---

## Analysis and Visualizations
The following analyses were performed:
- Subject-wise average score analysis (Bar Chart)
- Study hours vs score analysis (Line Chart)

All generated charts are saved in the `visualizations/` folder.

---

## How to Run the Project
1. Install required libraries:
   ```
   pip install -r requirements.txt
   ```
2. Run the main program:
   ```
   python main.py
   ```
3. View generated charts in the `visualizations/` folder
4. Open `analysis_report.pdf` for detailed insights

---

## Key Insights
- Higher study hours generally lead to higher scores
- English shows the highest average performance
- Math requires additional academic focus

---

## Conclusion
This project shows how data analysis and visualization techniques
can be used to understand student performance and support
data-driven academic improvements.
