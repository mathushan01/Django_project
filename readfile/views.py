from django.shortcuts import render, redirect
import pandas as pd
# Create your views here. 
 
def home(request):
    
    #read csv files
    csv_file1 = pd.read_csv(r'C:\Users\mathushan\Desktop\dataset\Ganison_dataset_1.csv', encoding='utf-8', nrows=800000)
    csv_file2 = pd.read_csv(r'C:\Users\mathushan\Desktop\dataset\Ganison_dataset_2.csv', encoding='utf-8', nrows=800000)
    csv_file3 = pd.read_csv(r'C:\Users\mathushan\Desktop\dataset\Ganison_dataset_3.csv', encoding='utf-8', nrows=800000)
    csv_file5 = pd.read_csv(r'C:\Users\mathushan\Desktop\dataset\Ganison_dataset_5.csv', encoding='utf-8', nrows=800000)    
    
    
    #combine all csv file datas
    combined_csv = pd.concat([csv_file1, csv_file2, csv_file3, csv_file5], ignore_index=True)
    
    
   
    #csv_file1 = pd.read_csv(r'C:\Users\mathushan\Desktop\dataset\Ganison_dataset_1.csv', encoding='utf-8')
    #csv_file2 = pd.read_csv(r'C:\Users\mathushan\Desktop\dataset\Ganison_dataset_2.csv', encoding='utf-8')
    #csv_file3 = pd.read_csv(r'C:\Users\mathushan\Desktop\dataset\Ganison_dataset_3.csv', encoding='utf-8')
    #csv_file4 = pd.read_csv(r'C:\Users\mathushan\Desktop\dataset\Ganison_dataset_4.csv', encoding='utf-8')
    #csv_file5 = pd.read_csv(r'C:\Users\mathushan\Desktop\dataset\Ganison_dataset_5.csv', encoding='utf-8')
    #csv_file6 = pd.read_csv(r'C:\Users\mathushan\Desktop\dataset\Ganison_dataset_6.csv', encoding='utf-8')
    #combined_csv = pd.concat([csv_file1, csv_file2, csv_file3, csv_file4, csv_file5, csv_file6], ignore_index=True)
    
    
    #create the full name
    def combine_columns(row):
        return str(row['First Name']) + " " + row['Last Name']
    
    
    # separate the columns
    school = combined_csv[['school_name']]
    school = school.drop_duplicates()
    
    class_data = combined_csv[['Class']]
    class_data = class_data.drop_duplicates()
    
    assessmentAreas = combined_csv[['Assessment Areas']]
    assessmentAreas = assessmentAreas.drop_duplicates()
    
    fullname = combined_csv[['First Name', 'Last Name']]
    fullname['Fullname'] = fullname.apply(combine_columns, axis=1)
    fullname = fullname[['Fullname']]
    fullname = fullname.drop_duplicates()
    
    answer = combined_csv[['Answers']]
    answer = answer.drop_duplicates()
    
    award = combined_csv[['award']]
    award = award.drop_duplicates()
    
    subject = combined_csv[['Subject Contents']]
    subject = subject.drop_duplicates()
    
    #summary = combined_csv[['sydney_participants', 'sydney_percentile', 'correct_answer_percentage_per_class', 'Correct Answers', 'StudentID', 'participant', 'student_score', 'Year Level', 'Answers', ]]
    #summary = summary.drop_duplicates()
    
    # send the data for index.html page
    return render(request,"readfile/index.html",{"school":school, "class_data":class_data, 'assessmentAreas':assessmentAreas, 'fullname':fullname, 'answer':answer, 'award':award, 'subject':subject})
