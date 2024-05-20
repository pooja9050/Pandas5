#184. Department Highest Salary
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    result = []
    for i in range(len(employee)):
        salary = employee['salary'][i]
        if salary not in result:
            result.append(salary)
    result.sort(reverse=True)
    if N > len(result) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    return pd.DataFrame({f'getNthHighestSalary({N})' : [result[N-1]]})

#Return null
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    resultSet = set()
    for i in range(len(employee)):
        salary = employee['salary'][i]
        resultSet.add(salary)
    result = []
    for element in resultSet:
        result.append(element)
    result.sort(reverse=True)
    if N > len(result) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    return pd.DataFrame({f'getNthHighestSalary({N})' : [result[N-1]]})

#Return null
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee[['salary']].drop_duplicates()
    if N > len(df) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    df = df.sort_values(by='salary',ascending=False,inplace=False)
    return df.head(N).tail(1)[['salary']].rename(columns={'salary':f'getNthHighestSalary({N})'})


#176. Second Highest Salary
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if employee["salary"].nunique() < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    nth = sorted(employee["salary"].unique(), reverse=True)[1]
    return pd.DataFrame({"SecondHighestSalary": [nth]})

#Alternative
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee[['salary']].drop_duplicates()
    if 2 > len(df):
        return pd.DataFrame({'SecondHighestSalary':[None]})
    df = df.sort_values(by=['salary'], ascending = False)
    df = df.head(2).tail(1)[['salary']].rename(columns = {'salary':'SecondHighestSalary'})
    return df
