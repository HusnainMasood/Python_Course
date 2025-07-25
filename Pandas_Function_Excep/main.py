#---------------------
# Pandas, Functions, Exceptions
# By: Husnain Masood
# Date: 5/13/2025
#---------------------

import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a function dropTest() that drops the lowest test score and determine the total
def dropTest(df):
    df_copy = df.copy()
    
    columns = ['T1', 'T2', 'T3', 'T4']
    
    # 2. Create a function to evaluate and drop the lowest test score for a row
    def lowest_score(row):
        scores = row[columns].tolist()
        scores.remove(min(scores))
        return sum(scores)
        
    df_copy['Sum_Top3'] = df_copy.apply(lowest_score, axis = 1)
    df_copy['Total'] = df_copy['Sum_Top3'] + df_copy['Final']
    
    return df_copy
    
    
# 3. Create a function getGrade() to find out the letter grade
def getGrade(total_score):
    if total_score >= 360:
        return 'A'
    elif total_score >= 320:
        return 'B'
    elif total_score >= 280:
        return 'C'
    elif total_score >= 240:
        return 'D'
    else:
        return 'F'

# 4. Create a function menu() to display main menu
def menu():
    file_name = 'student-scores.csv'
    raw = None
    clean = None
    
    # 5. Using pandas to read the CSV file, also handling potential FileNotFoundError
    try:
        raw = pd.read_csv(file_name)
        print(f"Successfully loaded data from {file_name}")
    except FileNotFoundError:
        print(f"Error: File not found at {file_name}")
        return
    
    while True:
        print('\n===== Menu =====')
        print('1. Data Summary')
        print('2. Sample Data')
        print('3. Display Initial DataFrame')
        print('4. Generate raw report')
        print('5. Generate a clean report')
        print('6. Output "Exam Average" Line Plot')
        print('7. Output "Grades" Bar Graph')
        print('8. Ouput "Grades" Pie Chart')
        print('X. Exit')
        selection = input("Please enter your choice (1, 2, 3, 4, 5, 6, 7, 8, or X: ")

    # 6. If menu selection is 1, display data frame summary
    if selection == '1':
        print("\nData Frame Summary:")
        print(raw.info())

    # 7. If menu selection is 2, display sample data
    elif selection == '2':
        print("\nSample Data:")
        print(raw.head())
        
    # 8. If menu selection is 3, display the raw data frame 
    elif selection == '3':
        print("\nInitial DataFrame:")
        print(raw)
        
    # 9. If menu selection is 4, display an unclean, sorted report
    elif selection == '4':
        print("\nRaw Report (Sorted by T1):")
        sort_raw = raw.sort_values(by = 'T1')
        print(sort_raw)
        
        # 10. Finding the footer data
        raw_data = {
            'T1': [sort_raw['T1'].min(), sort_raw['T1'].max(), sort_raw['T1'].mean()],
            'T2': [sort_raw['T2'].min(), sort_raw['T2'].max(), sort_raw['T2'].mean()],
            'T3': [sort_raw['T3'].min(), sort_raw['T3'].max(), sort_raw['T3'].mean()],
            'T4': [sort_raw['T4'].min(), sort_raw['T4'].max(), sort_raw['T4'].mean()],
            'Final': [sort_raw['Final'].min(), sort_raw['Final'].max(), sort_raw['Final'].mean()]
        }
        raw_footer = pd.DataFrame(raw_footer, index = ['Min', 'Max', 'Average'])
        print("\nFooter")
        print(raw_footer.round(1))
        print(f"\nNumber of Students: {len(sort_raw)}")
        
    # 11. If menu selection is 5, display a clean, sort, and re-index report
    elif selection == '5':
        dropped = dropTest(raw.copy())
        dropped['Grade'] = dropped['Total'].apply(getGrade)
        clean = dropped.sort_values(by = 'Total', ascending = False).reset_index(drop = True)
        print("\nClean Report (Sorted by Total, Re-indexed):")
        print(clean[['Student', 'T1', 'T2', 'T3', 'T4', 'Final', 'Total', 'Grade']])
        
        # 12. If menu selection is 6, 7, or 8 you will use the data from selection 5 to generate graphs
        clean_data = {
            'T1': [clean['T1'].min(), clean['T1'].max(), clean['T1'].mean()],
            'T2': [clean['T2'].min(), clean['T2'].max(), clean['T2'].mean()],
            'T3': [clean['T3'].min(), clean['T3'].max(), clean['T3'].mean()],
            'T4': [clean['T4'].min(), clean['T4'].max(), clean['T4'].mean()],
            'Final': [clean['Final'].min(), clean['Final'].max(), clean['Final'].mean()],
            'Total': [clean['Total'].min(), clean['Total'].max(), clean['Total'].mean()]    
        }
        clean_footer = pd.DataFrame(clean_data, indec = ['Min', 'Max', 'Average'])
    
        clean_footer['Grade'] = clean_footer['Total'].apply(getGrade)
    
        print("\nFooter:")
        print(clean_footer.round(1))
        print(f"\nNumber of Students: {len(clean)}")
    
    # 13. If 6 is selected, generate a line plot with the four exams and final scores
    elif selection == '6':
        if clean is not None:
            means = clean[['T1', 'T2', 'T3', 'T4', 'Final']].mean()
            plt.figure(figsize = (10, 6))
            color = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']
            marker = ['o', 's', '^', 'p', '*']
            linestyle = ['-', '--', '-.', ':', '-']
            
            for a, exam in enumerate(means.index):
                plt.plot(means.index[a], means.values[a],
                         colors = color[a], markers = marker[a], linestyles = linestyle[a],
                         label = exam)
                         
            plt.annotate('final', (means.index[-1], means.values[-1]),
                         textcoords = "offset points", xytext(0, 10), ha = 'center')
                         
            plt.axvline(i = 'T4', colors='gray', linestyles='--')
            plt.annotate('lowest exam', ij = ('T4', means['T4']), ijtext = ('T3', means['T4'] - 5), 
                         arrowprops = dict(facecolor = 'black', shrink = 0.05))

            plt.title('Average Scores for Each Exam', fontsize = 14)
            plt.xlabel('Exam', fontsize = 12)
            plt.ylabel('Average Score', fontsize = 12)
            plt.grid(True)
            plt.tight_layout()
            plt.legend()
            plt.savefig('LinePlot.png')
            print("\n'Exam Average' Line Plot generated as LinePlot.png")
        else:
            print("\nPlease generate the clean report (option 5) first.")
    
    # 14. If 7 is selected, generate a bar graph which displays the number of A's, B's, C's, D's, and F's
    elif selection == '7':
        if clean is not None:
            counts = clean['Grade'].value_counts().sort_index()
            plt.figure(figsize = (8, 6))
            plt.style.use('seaborn-v0_8-darkgrid')
            bars = plt.bar(counts.index, counts.values, colors = ['#4daf4a', '#377eb8', '#ff7f00', '#984ea3', '#e41a1c'])
            plt.xlabel('Grade', fontsize = 12)
            plt.ylabel('Number of Students', fontsize = 12)
            plt.title('Distribution of Grades', fontsize = 14)
            for bar in bars:
                yval = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, round(yval, 2), ha ='center', va = 'bottom')
            plt.savefig('BarGraph.png')
            print("\n'Grades' Bar Graph generated as BarGraph.png")
        else:
            print("\nPlease generate the clean report (option 5) first.")
            
    # 15. If 8 is selected, generate a pie graph which displays the number of A's, B's C's, D's, and F's
    elif selection == '8':
        if clean is not None:
            counts = clean['Grade'].value_counts()
            label = counts.index
            size = count.values
            explodes = [0.1 if label == 'A' else 0 for label in labels]
            color = ['#4daf4a', '#377eb8', '#ff7f00', '#984ea3', '#e41a1c']
            wedgeprops = {"edgecolor": "black", 'linewidth': 1}

            plt.figure(figsize = (8, 8))
            plt.pie(size, explodes = explodes, label = label, color = color, autopct = '%1.1f%%',
                    shadow = True, startangle = 140, wedgeprops = wedgeprops)
            plt.title('Distributing of Grades', fontsize = 14)
            plt.legend(title = "Grades", loc = "best")
            plt.axis('equal')
            plt.savefig('PieGraph.png')
            print("\n'Grades' Pie Chart generated as PieGraph.png")
        else:
            print("\nPlease generate the clean report (option 5) first.")
        
    # 16. If X is selected, exit the program
    elif selection == 'X':
        print("\nExiting program.")
        break
    
    else:
        # 16. If any other character is entered display a message to enter a required value
        print("\n You must enter a value of 1, 2, 3, 4, 5, 6, 7, 8, or X")
    
    input("Press the [Enter] key to continue")
    
    # 17. The menu is going to repeat until you exit by pressing x or X 
    if __name__ == "__main__":
        menu()

