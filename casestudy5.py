import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry']
math_scores = [85, 90, 78, 92, 88, 76, 95, 82]
science_scores = [88, 85, 80, 89, 91, 79, 93, 86]
english_scores = [92, 88, 85, 87, 86, 82, 89, 90]

data = {
    'Student': students,
    'Math': math_scores,
    'Science': science_scores,
    'English': english_scores
}
df = pd.DataFrame(data)


df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1).round(2)
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

print("=== STUDENT PERFORMANCE DATA ===\n")
print(df.to_string(index=False))


print("\n=== STATISTICS ===\n")
print("Subject Averages:")
print(f"Math: {df['Math'].mean():.2f}")
print(f"Science: {df['Science'].mean():.2f}")
print(f"English: {df['English'].mean():.2f}")

print("\nSubject Min-Max:")
print(f"Math: {df['Math'].min()} - {df['Math'].max()}")
print(f"Science: {df['Science'].min()} - {df['Science'].max()}")
print(f"English: {df['English'].min()} - {df['English'].max()}")


print("\n=== TOP 3 STUDENTS ===")
top_3 = df.nlargest(3, 'Average')[['Student', 'Average']]
print(top_3.to_string(index=False))

print("\n=== BOTTOM 3 STUDENTS ===")
bottom_3 = df.nsmallest(3, 'Average')[['Student', 'Average']]
print(bottom_3.to_string(index=False))

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

subjects = ['Math', 'Science', 'English']
averages = [df['Math'].mean(), df['Science'].mean(), df['English'].mean()]
axes[0, 0].bar(subjects, averages, color=['blue', 'green', 'red'])
axes[0, 0].set_title('Average Scores by Subject')
axes[0, 0].set_ylabel('Score')
axes[0, 0].set_ylim(0, 100)

for i, student in enumerate(students):
    scores = [df.loc[i, 'Math'], df.loc[i, 'Science'], df.loc[i, 'English']]
    axes[0, 1].plot(subjects, scores, marker='o', label=student)
axes[0, 1].set_title('Student Scores by Subject')
axes[0, 1].set_ylabel('Score')
axes[0, 1].legend(fontsize=8)
axes[0, 1].set_ylim(70, 100)

all_scores = df[['Math', 'Science', 'English']].values.flatten()
axes[1, 0].hist(all_scores, bins=10, color='purple', edgecolor='black')
axes[1, 0].set_title('Score Distribution')
axes[1, 0].set_xlabel('Score')
axes[1, 0].set_ylabel('Frequency')


grade_counts = [
    len(df[df['Average'] >= 90]),
    len(df[(df['Average'] >= 80) & (df['Average'] < 90)]),
    len(df[df['Average'] < 80])
]
grades = ['A (90+)', 'B (80-89)', 'C (<80)']
axes[1, 1].pie(grade_counts, labels=grades, autopct='%1.1f%%', colors=['gold', 'silver', 'brown'])
axes[1, 1].set_title('Grade Distribution')

plt.tight_layout()
plt.savefig('student_analysis.png', dpi=150)
plt.show()

print("\n✓ Visualization saved as 'student_analysis.png'")