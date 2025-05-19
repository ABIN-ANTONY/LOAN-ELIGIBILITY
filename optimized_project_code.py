# importing all required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn  as sns

df = pd.read_csv("Financial_data.csv")
pd.set_option("display.max_columns",112)
df

## finding the shape of the dataset which is the total rows and columns
df.shape

df.head()

df.tail()

## viewing the column names in the dataset
df.columns

## metadata of the dataframe
df.info()

## viewing the Statistical summary of all numerical columns
df.describe()

df['DefaultStatus'] = df['DefaultDate'].notna().astype(int)
df['DefaultStatus'] = df['DefaultStatus'].replace({0:'Not default',1:'Default'})
df
# df['DefaultDate']=df['DefaultDate'].fillna('Nil')
# df['DefaultStatus']=np.where(df['DefaultDate']=='Nil','Not Default','Default')
# df['DefaultDate'].drop
# df

## Dropping of unwanted columns from the dataset 
# frirstly dropping the columns with null values havig a percentage above 40%
# after dropping of them secondly dropping off the columns which seems unwanted after studying each column

## getting null values with values above 40%
columnswith40 =[]
for i in df:
    perc = (df[i].isnull().sum()/df.shape[0])*100
    if perc > 40:
        columnswith40.append(i)
print(columnswith40)

len(columnswith40)

# dropping the columns having null values more than 40%.
df1 = df.drop(columnswith40,axis=1)
df1

# dropping the columns which seems unwanted after studying each columns from the updated dataset
# description on the reason why the columns are getting droped from the data set 
# 1.ReportAsOfEOD - 
#

irreleventcolumns = ["LoanId","ListedOnUTC","BiddingStartedOn","LoanNumber","LoanApplicationStartedDate","LoanDate","FirstPaymentDate","MaturityDate_Original",
                     "DateOfBirth","IncomeFromPrincipalEmployer","IncomeFromPension","IncomeFromFamilyAllowance","IncomeFromSocialWelfare",
                     "IncomeFromLeavePay","IncomeFromChildSupport","IncomeOther","ActiveScheduleFirstPaymentReached","LastPaymentOn","ExpectedLoss","StageActiveSince",
                     "ModelVersion","ReportAsOfEOD","UserName","ApplicationSignedHour",	"ApplicationSignedWeekday","MaturityDate_Last","LossGivenDefault","ProbabilityOfDefault"]
df3 = df1.drop(irreleventcolumns,axis = 1)
df3

## handling null values
# Methods for Handling Null Values
# *Imputation Methods
#     * Mean Imputation
#     * Median Imputation
#     * Mode Imputation
# * Dropping Null Values

df3.isnull().sum()

df3

df3.dtypes

# converting the null percentage of each columns
##1.verification type
df3['VerificationType']= df3['VerificationType'].astype('float')

# finding mean of VerificationType
VerificationType_mode=df3["VerificationType"].mode()[0]
VerificationType_mode

## filling the null values with the mode values
df3['VerificationType']= df3['VerificationType'].fillna(VerificationType_mode)

##1.verification type
df3['VerificationType']= df3['VerificationType'].astype('int')

df3

# converting the null percentage of each columns
##2.Gender
df3['Gender']= df3['Gender'].astype('float')

# finding mode of Gender
Gender_mode=df3["Gender"].mode()[0]
Gender_mode

## filling the null values with the mode values
df3['Gender']= df3['Gender'].fillna(Gender_mode)

# converting the null percentage of each columns
df3['Gender']= df3['Gender'].astype('int')

df3

# converting the null percentage of each columns
##3.MonthlyPayment
df3['MonthlyPayment']= df3['MonthlyPayment'].astype('float')

# finding mean of MonthlyPayment
MonthlyPayment_mode=df3["MonthlyPayment"].mean()
MonthlyPayment_mode

## filling the null values with the mode values
df3['MonthlyPayment']= df3['MonthlyPayment'].fillna(MonthlyPayment_mode)

df3

# converting the null percentage of each columns
##4.County
df3['County']= df3['County'].astype('object')

# finding mode of MonthlyPayment
County_mode=df3["County"].mode()[0]
County_mode

## filling the null values with the mode values
df3['County']= df3['County'].fillna(County_mode)

df3

# converting the null percentage of each columns
##5.City
df3['City']= df3['City'].astype('object')

# finding mode of City
City_mode=df3["City"].mode()[0]
City_mode

## filling the null values with the mode values
df3['City']= df3['City'].fillna(City_mode)

df3

# converting the null percentage of each columns
##7.Education
df3['Education']= df3['Education'].astype('float')

# finding mode of Education
Education_mode=df3["Education"].mode()[0]
Education_mode

## filling the null values with the mode values
df3['Education']= df3['Education'].fillna(Education_mode)

df3

# converting the null percentage of each columns
##8.MaritalStatus
df3['MaritalStatus']= df3['MaritalStatus'].astype('float')

# finding mode of MaritalStatus
MaritalStatus_mode=df3["MaritalStatus"].mode()[0]
MaritalStatus_mode

## filling the null values with the mode values
df3['MaritalStatus']= df3['MaritalStatus'].fillna(MaritalStatus_mode)

df3['MaritalStatus']= df3['MaritalStatus'].astype('int')

df3

# converting the null percentage of each columns
##8.EmploymentStatus
df3['EmploymentStatus']= df3['EmploymentStatus'].astype('float')

# finding mode of MaritalStatus
EmploymentStatus_mode=df3["EmploymentStatus"].mode()[0]
EmploymentStatus_mode

## filling the null values with the mode values
df3['EmploymentStatus']= df3['EmploymentStatus'].fillna(MaritalStatus_mode)

df3

# converting the null percentage of each columns
##8.EmploymentDurationCurrentEmployer
df3['EmploymentDurationCurrentEmployer']= df3['EmploymentDurationCurrentEmployer'].astype('object')

# finding mode of EmploymentDurationCurrentEmployer
EmploymentDurationCurrentEmployer_mode=df3["EmploymentDurationCurrentEmployer"].mode()[0]
EmploymentDurationCurrentEmployer_mode

## filling the null values with the mode values
df3['EmploymentDurationCurrentEmployer']= df3['EmploymentDurationCurrentEmployer'].fillna(MaritalStatus_mode)

df3

# converting the null percentage of each columns
##8.OccupationArea
df3['OccupationArea']= df3['OccupationArea'].astype('float')

# finding mode of EmploymentDurationCurrentEmployer
OccupationArea_mode=df3["OccupationArea"].mode()[0]
OccupationArea_mode

## filling the null values with the mode values
df3['OccupationArea']= df3['OccupationArea'].fillna(OccupationArea_mode)

df3

# converting the null percentage of each columns
##9.HomeOwnershipType
df3['HomeOwnershipType']= df3['HomeOwnershipType'].astype('float')

# finding mode of HomeOwnershipType
HomeOwnershipType_mode=df3["HomeOwnershipType"].mode()[0]
HomeOwnershipType_mode

## filling the null values with the mode values
df3['HomeOwnershipType']= df3['HomeOwnershipType'].fillna(HomeOwnershipType_mode)

df3

# converting the null percentage of each columns
##10.DebtToIncome
df3['DebtToIncome']= df3['DebtToIncome'].astype('float')

# finding mode of DebtToIncome
DebtToIncome_mean=df3["DebtToIncome"].mean()
DebtToIncome_mean

## filling the null values with the mode values
df3['DebtToIncome']= df3['DebtToIncome'].fillna(DebtToIncome_mean)

df3

# converting the null percentage of each columns
##1.Free cash
df3['FreeCash']= df3['FreeCash'].astype('float')

# finding mean of free cash
free_mean=df3["FreeCash"].mean()
free_mean

## filling the null values with the mean values
df3['FreeCash']= df3['FreeCash'].fillna(free_mean)

df3

##2PlannedInterestTillDate
df3['PlannedInterestTillDate']= df3['PlannedInterestTillDate'].astype('float')

# finding mean of PlannedInterestTillDate
PlannedInterestTillDate_mean=df3["PlannedInterestTillDate"].mean()
PlannedInterestTillDate_mean

## filling the null values with the mean values
df3['PlannedInterestTillDate']= df3['PlannedInterestTillDate'].fillna(PlannedInterestTillDate_mean)

df3

# finding mean of ExpectedReturn
ExpectedReturn_mean=df3["ExpectedReturn"].mean()
ExpectedReturn_mean

## filling the null values with the mean values
df3['ExpectedReturn']= df3['ExpectedReturn'].fillna(ExpectedReturn_mean)

df3

# finding mean of PrincipalOverdueBySchedule
PrincipalOverdueBySchedule_mean=df3["PrincipalOverdueBySchedule"].mean()
PrincipalOverdueBySchedule_mean

## filling the null values with the mean values
df3['PrincipalOverdueBySchedule']= df3['PrincipalOverdueBySchedule'].fillna(PrincipalOverdueBySchedule_mean)

df3

# finding mean of Rating
Rating_mode=df3["Rating"].mode()[0]
Rating_mode

## filling the null values with the mean values
df3['Rating']= df3['Rating'].fillna(Rating_mode)

df3

# finding mean of WorseLateCategory
WorseLateCategory_mode=df3["WorseLateCategory"].mode()[0]
WorseLateCategory_mode

## filling the null values with the mean values
df3['WorseLateCategory']= df3['WorseLateCategory'].fillna(WorseLateCategory_mode)

df3

# finding mean of CreditScoreEsMicroL
CreditScoreEsMicroL_mode=df3["CreditScoreEsMicroL"].mode()[0]
CreditScoreEsMicroL_mode

## filling the null values with the mean values
df3['CreditScoreEsMicroL']= df3['CreditScoreEsMicroL'].fillna(CreditScoreEsMicroL_mode)

df3

# finding mean of PreviousRepaymentsBeforeLoan
PreviousRepaymentsBeforeLoan_mean=df3["PreviousRepaymentsBeforeLoan"].mean()
PreviousRepaymentsBeforeLoan_mean

## filling the null values with the mean values
df3['PreviousRepaymentsBeforeLoan']= df3['PreviousRepaymentsBeforeLoan'].fillna(PreviousRepaymentsBeforeLoan_mean)

df3

# finding mean of NextPaymentNr
NextPaymentNr_mean=df3["NextPaymentNr"].mean()
NextPaymentNr_mean

## filling the null values with the mean values
df3['NextPaymentNr']= df3['NextPaymentNr'].fillna(NextPaymentNr_mean)

df3

# finding mean of NextPaymentNr
NextPaymentNr_mean=df3["NextPaymentNr"].mean()
NextPaymentNr_mean

## filling the null values with the mean values
df3['NextPaymentNr']= df3['NextPaymentNr'].fillna(NextPaymentNr_mean)

##2.DebtToIncome
df3['DebtToIncome']= df3['DebtToIncome'].astype('float')

# finding mean of NrOfScheduledPayments
NrOfScheduledPayments_mean=df3["NrOfScheduledPayments"].mean()
NrOfScheduledPayments_mean

## filling the null values with the mean values
df3['NrOfScheduledPayments']= df3['NrOfScheduledPayments'].fillna(NrOfScheduledPayments_mean)

df3

##3.MonthlyPayment
df3['MonthlyPayment']= df3['MonthlyPayment'].astype('float')

# finding mean of MonthlyPayment
MonthlyPayment_mean=df3["MonthlyPayment"].mean()
MonthlyPayment_mean

## filling the null values with the mean values
df3['MonthlyPayment']= df3['MonthlyPayment'].fillna(MonthlyPayment_mean)

df3

##4.EmploymentStatus
df3['EmploymentStatus']= df3['EmploymentStatus'].astype('float')

# finding mean of EmploymentStatus
EmploymentStatus_mean=df3["EmploymentStatus"].mean()
EmploymentStatus_mean

## filling the null values with the mean values
df3['EmploymentStatus']= df3['EmploymentStatus'].fillna(EmploymentStatus_mean)

df3['EmploymentStatus']= df3['EmploymentStatus'].astype('int')

df3

##4.MaritalStatus 
df3['MaritalStatus']= df3['MaritalStatus'].astype('float')

# finding mean of MaritalStatus
MaritalStatus_mode=df3["MaritalStatus"].mode()[0]
MaritalStatus_mode

## filling the null values with the mean values
df3['MaritalStatus']= df3['MaritalStatus'].fillna(MaritalStatus_mode)

df3['MaritalStatus']= df3['MaritalStatus'].astype('int')

df3

df3.isnull().sum()

df3.duplicated().sum()

df3.drop_duplicates(inplace=True)

df3.duplicated().sum()

df3 = df3.reset_index(drop=True)
df3

df3.dtypes

df3

# Univariate analysis of column BidsPortfolioManager	
sns.kdeplot(df3['BidsPortfolioManager'])
plt.show()

# Univariate analysis of column BidsApi	
sns.kdeplot(df3['BidsApi'])
plt.show()

# Univariate analysis of column BidsManual	
sns.kdeplot(df3['BidsManual'])
plt.show()

# Univariate analysis of column AppliedAmount	
sns.kdeplot(df3['AppliedAmount'])
plt.show()

# Univariate analysis of column Amount	
sns.kdeplot(df3['Amount'])
plt.show()

# Univariate analysis of column Interest	
sns.kdeplot(df3['Interest'])
plt.show()

# Univariate analysis of column MonthlyPayment	
sns.kdeplot(df3['MonthlyPayment'])
plt.show()

# Univariate analysis of column LiabilitiesTotal	
df["OccupationArea"].value_counts().plot(kind='bar')
plt.show()

# Univariate analysis of column LiabilitiesTotal	
df["HomeOwnershipType"].value_counts().plot(kind='bar')
plt.show()

# Univariate analysis of column IncomeTotal	
sns.kdeplot(df3['IncomeTotal'])
plt.show()

# Univariate analysis of column LoanDuration	
sns.kdeplot(df3['LoanDuration'])
plt.show()

df["RefinanceLiabilities"].value_counts().plot(kind='bar')
plt.show()

df["ExistingLiabilities"].value_counts().plot(kind='bar')
plt.show()

df["Gender"].value_counts().plot(kind='bar')
plt.show()

df["Country"].value_counts().plot(kind='bar')
plt.show()

df["Education"].value_counts().plot(kind='bar')
plt.show()

# Univariate analysis of column LiabilitiesTotal	
sns.kdeplot(df3['MonthlyPayment'])
plt.show()

# Univariate analysis of column LiabilitiesTotal	
df["WorseLateCategory"].value_counts().plot(kind='bar')
plt.show()

# Univariate analysis of column LiabilitiesTotal	
sns.kdeplot(df3['LiabilitiesTotal'])
plt.show()

# Univariate analysis of column MonthlyPayment	
sns.kdeplot(df3['DebtToIncome'])
plt.show()

# Univariate analysis of column FreeCash	
sns.kdeplot(df3['FreeCash'])
plt.show()

# Univariate analysis of column PlannedInterestTillDate	
sns.kdeplot(df3['PlannedInterestTillDate'])
plt.show()

# Univariate analysis of column ExpectedReturn	
sns.kdeplot(df3['ExpectedReturn'])
plt.show()

# Univariate analysis of column PrincipalOverdueBySchedule	
sns.kdeplot(df3['PrincipalOverdueBySchedule'])
plt.show()

# Univariate analysis of column PrincipalPaymentsMade	
sns.kdeplot(df3['PrincipalPaymentsMade'])
plt.show()

# Univariate analysis of column PrincipalBalance	
sns.kdeplot(df3['PrincipalBalance'])
plt.show()

# Univariate analysis of column InterestAndPenaltyPaymentsMade	
sns.kdeplot(df3['InterestAndPenaltyPaymentsMade'])
plt.show()

# Univariate analysis of column AmountOfPreviousLoansBeforeLoan	
sns.kdeplot(df3['AmountOfPreviousLoansBeforeLoan'])
plt.show()

# Univariate analysis of column NextPaymentNr	
sns.kdeplot(df3['NextPaymentNr'])
plt.show()

# Univariate analysis of column NrOfScheduledPayments	
sns.kdeplot(df3['NrOfScheduledPayments'])
plt.show()

# Univariate analysis of column IncomeTotal	
sns.kdeplot(df3['IncomeTotal'])
plt.show()

df["NewCreditCustomer"].value_counts().plot(kind='bar')
plt.show()

df["VerificationType"].value_counts().plot(kind='bar')
plt.show()

df["LanguageCode"].value_counts().plot(kind='bar')
plt.show()

# f = plt.figure()
# f.set_figwidth(20)
# f.set_figheight(10)
# df["County"].value_counts().plot(kind='bar')
# plt.xticks(rotation=90)
# plt.show()

# f = plt.figure()
# f.set_figwidth(20)
# f.set_figheight(10)

# df["City"].value_counts().plot(kind='bar')
# plt.xticks(rotation=90)
# plt.show()

df["UseOfLoan"].value_counts().plot(kind='bar')
plt.show()

df["UseOfLoan"]=df["UseOfLoan"].replace(-1,1)

df["UseOfLoan"].value_counts().plot(kind='bar')
plt.show()

df["Education"].value_counts().plot(kind='bar')
plt.show()

df=df[df["Education"] !=-1]

df["Education"].value_counts().plot(kind='bar')
plt.show()

df["MaritalStatus"].value_counts().plot(kind='bar')
plt.show()

df["MaritalStatus"]=df["MaritalStatus"].replace(-1,1)

df["MaritalStatus"].value_counts().plot(kind='bar')
plt.show()

df["EmploymentStatus"].value_counts().plot(kind='bar')
plt.show()

df["EmploymentStatus"]=df["EmploymentStatus"].replace(-1,1)

df["EmploymentStatus"].value_counts().plot(kind='bar')
plt.show()

df["EmploymentDurationCurrentEmployer"].value_counts().plot(kind='bar')
plt.show()

df["Rating"].value_counts().plot(kind='bar')
plt.show()

df["Status"].value_counts().plot(kind='bar')
plt.show()

df["Restructured"].value_counts().plot(kind='bar')
plt.show()

df["CreditScoreEsMicroL"].value_counts().plot(kind='bar')
plt.show()

df["NoOfPreviousLoansBeforeLoan"].value_counts().plot(kind='bar')
plt.show()

df["NewCreditCustomer"].value_counts().plot(kind='bar')
plt.show()

df["Country"].value_counts().plot(kind='bar')
plt.show()

sns.kdeplot(df3['Age'])
plt.show()

df["DefaultStatus"].value_counts().plot(kind='bar')
plt.show()

df["DefaultStatus"].value_counts()

df3

# bivariate analysis of BidsPortfolioManager and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="BidsPortfolioManager")
plt.title("BidsPortfolioManager V/S DefaultStatus")
plt.show()

# bivariate analysis of BidsPortfolioManager and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="BidsApi")
plt.title("BidsApi V/S DefaultStatus")
plt.show()

# bivariate analysis of BidsManual and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="BidsManual")
plt.title("BidsManual V/S DefaultStatus")
plt.show()

# bivariate analysis of NewCreditCustomer and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["NewCreditCustomer"])

# bivariate analysis of VerificationType and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["VerificationType"])

# bivariate analysis of LanguageCode and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["LanguageCode"])

# bivariate analysis of Age and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="Age")
plt.title("Age V/S DefaultStatus")
plt.show()

# bivariate analysis of Gender and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["Gender"])

# # bivariate analysis of Country and DefaultStatus
# pd.crosstab(df["DefaultStatus"],df["Country"])

# bivariate analysis of AppliedAmount and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="AppliedAmount")
plt.title("AppliedAmount V/S DefaultStatus")
plt.show()

# bivariate analysis of AppliedAmount and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="Amount")
plt.title("Amount V/S DefaultStatus")
plt.show()

# bivariate analysis of Interest and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="Interest")
plt.title("Interest V/S DefaultStatus")
plt.show()

# bivariate analysis of Loanduration and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="LoanDuration")
plt.title("Loanduration V/S DefaultStatus")
plt.show()

# bivariate analysis of Loanduration and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="MonthlyPayment")
plt.title("MonthlyPayment V/S DefaultStatus")
plt.show()

# # bivariate analysis of County and DefaultStatus
# pd.crosstab(df["DefaultStatus"],df["County"])

# # bivariate analysis of City and DefaultStatus
# pd.crosstab(df["DefaultStatus"],df["City"])

# bivariate analysis of Useofloan and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["UseOfLoan"])

# bivariate analysis of Education and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["Education"])

# bivariate analysis of Maritalstatus and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["MaritalStatus"])

# bivariate analysis of Employmentstatus and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["EmploymentStatus"])

# bivariate analysis of Employmentduration and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["EmploymentDurationCurrentEmployer"])

# bivariate analysis of Occupationare and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["OccupationArea"])

# bivariate analysis of HomeOwnershipType and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["HomeOwnershipType"])

# bivariate analysis of IncomeTotal and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="IncomeTotal")
plt.title("IncomeTotal V/S DefaultStatus")
plt.show()

# bivariate analysis of ExistingLiabilities and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["ExistingLiabilities"])

# bivariate analysis of LiabilitiesTotal and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="LiabilitiesTotal")
plt.title("LiabilitiesTotal V/S DefaultStatus")
plt.show()

# bivariate analysis of RefinanceLiabilities and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["RefinanceLiabilities"])

# bivariate analysis of DebtToIncome and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="DebtToIncome")
plt.title("DebtToIncome V/S DefaultStatus")
plt.show()

# bivariate analysis of Freecash and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="FreeCash")
plt.title("Freecash V/S DefaultStatus")
plt.show()

# bivariate analysis of MonthlyPaymemnt and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="MonthlyPayment")
plt.title("MonthlyPaymemnt V/S DefaultStatus")
plt.show()

# bivariate analysis of PlannedInterestTillDate and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="PlannedInterestTillDate")
plt.title("PlannedInterestTillDate V/S DefaultStatus")
plt.show()

# bivariate analysis of ExpectedReturn and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="ExpectedReturn")
plt.title("ExpectedReturn V/S DefaultStatus")
plt.show()

# bivariate analysis of PrincipalOverdueBySchedule and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="PrincipalOverdueBySchedule")
plt.title("PrincipalOverdueBySchedule V/S DefaultStatus")
plt.show()

# bivariate analysis of Rating and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["Rating"])

# bivariate analysis of Status and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["Status"])

# bivariate analysis of Restructured and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["Restructured"])

# bivariate analysis of WorseLateCategory and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="WorseLateCategory")
plt.title("WorseLateCategory V/S DefaultStatus")
plt.show()

# bivariate analysis of CreditScoreEsMicroL and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["CreditScoreEsMicroL"])

# bivariate analysis of PrincipalPaymentsMade and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="PrincipalPaymentsMade")
plt.title("PrincipalPaymentsMade V/S DefaultStatus")
plt.show()

# bivariate analysis of InterestAndPenaltyPaymentsMade and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="InterestAndPenaltyPaymentsMade")
plt.title("InterestAndPenaltyPaymentsMade V/S DefaultStatus")
plt.show()

# bivariate analysis of PrincipalBalance and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="PrincipalBalance")
plt.title("PrincipalBalance V/S DefaultStatus")
plt.show()

# bivariate analysis of InterestAndPenaltyBalance and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="InterestAndPenaltyBalance")
plt.title("InterestAndPenaltyBalance V/S DefaultStatus")
plt.show()

# bivariate analysis of NoOfPreviousLoansBeforeLoan and DefaultStatus
pd.crosstab(df["DefaultStatus"],df["NoOfPreviousLoansBeforeLoan"])

# bivariate analysis of AmountOfPreviousLoansBeforeLoan and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="AmountOfPreviousLoansBeforeLoan")
plt.title("AmountOfPreviousLoansBeforeLoan V/S DefaultStatus")
plt.show()

# bivariate analysis of PreviousRepaymentsBeforeLoan and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="PreviousRepaymentsBeforeLoan")
plt.title("PreviousRepaymentsBeforeLoan V/S DefaultStatus")
plt.show()

# bivariate analysis of NextPaymentNr and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="NextPaymentNr")
plt.title("NextPaymentNr V/S DefaultStatus")
plt.show()

# bivariate analysis of NrOfScheduledPayments and DefaultStatus
sns.barplot(data=df3,x="DefaultStatus",y="NrOfScheduledPayments")
plt.title("NrOfScheduledPayments V/S DefaultStatus")
plt.show()

df3

## Multivariate analysis of
sns.barplot(data=df,x='NewCreditCustomer',y='Age',hue='DefaultStatus')
plt.title("NewCreditCustomer V/S Age V/S DefaultStatus")
plt.show()

# ## Multivariate analysis of
# sns.barplot(data=df,x='Status',y='FreeCash',hue='NewCreditCustomer')
# plt.title("Status V/S FreeCash V/S NewCreditCustomer")
# plt.show()

# ## Multivariate analysis of
# sns.scatterplot(data=df,x='Interest',y='AppliedAmount',hue='DefaultStatus')
# plt.title("Interest V/S AppliedAmount V/S DefaultStatus")
# plt.show()

# ## Multivariate analysis of
# sns.barplot(data=df,x='IncomeTotal',y='ExistingLiabilities',hue='DefaultStatus')
# plt.title("IncomeTotal V/S ExistingLiabilities V/S DefaultStatus")
# plt.show()

# ## Multivariate analysis of
# sns.barplot(data=df,x='Education',y='VerificationType',hue='DefaultStatus')
# plt.title("VerificationType V/S Education V/S DefaultStatus")
# plt.show()

# ## Multivariate analysis of
# sns.scatterplot(data=df,x='Interest',y='Amount',hue='DefaultStatus')
# plt.title("Amount V/S Interest V/S DefaultStatus")
# plt.show()

# ## Multivariate analysis of
# sns.barplot(data=df,x='LoanDuration',y='Amount',hue='DefaultStatus')
# plt.title("LoanDuration V/S Interest V/S DefaultStatus")
# plt.show()

# ## Multivariate analysis of
# sns.scatterplot(data=df,x='MonthlyPayment',y='NrOfScheduledPayments',hue='DefaultStatus')
# plt.title("MonthlyPayment V/S NrOfScheduledPayments V/S DefaultStatus")
# plt.show()

df3

sns.boxplot(df3['BidsManual'],orient='h')
plt.show()

q1=np.quantile(df3["BidsManual"],0.25)
q3=np.quantile(df3["BidsManual"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['BidsManual'])):
    if df3['BidsManual'][i]> max_bound:
        df3['BidsManual'][i]=max_bound

sns.boxplot(df3['BidsManual'],orient='h')
plt.show()

sns.boxplot(df3['AppliedAmount'],orient='h')
plt.show()

q1=np.quantile(df3["AppliedAmount"],0.25)
q3=np.quantile(df3["AppliedAmount"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['AppliedAmount'])):
    if df3['AppliedAmount'][i]> max_bound:
        df3['AppliedAmount'][i]=max_bound

sns.boxplot(df3['AppliedAmount'],orient='h')
plt.show()

sns.boxplot(df3['Age'],orient='h')
plt.show()

q1=np.quantile(df3["Age"],0.25)
q3=np.quantile(df3["Age"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['Age'])):
    if df3['Age'][i]> max_bound:
        df3['Age'][i]=max_bound

sns.boxplot(df3['Age'],orient='h')
plt.show()

sns.boxplot(df3['Amount'],orient='h')
plt.show()

q1=np.quantile(df3["Amount"],0.25)
q3=np.quantile(df3["Amount"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['Amount'])):
    if df3['Amount'][i]> max_bound:
        df3['Amount'][i]=max_bound

sns.boxplot(df3['Amount'],orient='h')
plt.show()

sns.boxplot(df3['Interest'],orient='h')
plt.show()

q1=np.quantile(df3["Interest"],0.25)
q3=np.quantile(df3["Interest"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['Interest'])):
    if df3['Interest'][i]> max_bound:
        df3['Interest'][i]=max_bound

sns.boxplot(df3['Interest'],orient='h')
plt.show()

sns.boxplot(df3['ExistingLiabilities'],orient='h')
plt.show()

q1=np.quantile(df3["ExistingLiabilities"],0.25)
q3=np.quantile(df3["ExistingLiabilities"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['ExistingLiabilities'])):
    if df3['ExistingLiabilities'][i]> max_bound:
        df3['ExistingLiabilities'][i]=max_bound

sns.boxplot(df3['ExistingLiabilities'],orient='h')
plt.show()

sns.boxplot(df3['MonthlyPayment'],orient='h')
plt.show()

q1=np.quantile(df3["MonthlyPayment"],0.25)
q3=np.quantile(df3["MonthlyPayment"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['MonthlyPayment'])):
    if df3['MonthlyPayment'][i]> max_bound:
        df3['MonthlyPayment'][i]=max_bound

sns.boxplot(df['MonthlyPayment'],orient='h')
plt.show()

sns.boxplot(df3['IncomeTotal'],orient='h')
plt.show()

q1=np.quantile(df3["IncomeTotal"],0.25)
q3=np.quantile(df3["IncomeTotal"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['IncomeTotal'])):
    if df3['IncomeTotal'][i]> max_bound:
        df3['IncomeTotal'][i]=max_bound

sns.boxplot(df3['IncomeTotal'],orient='h')
plt.show()

sns.boxplot(df3['LiabilitiesTotal'],orient='h')
plt.show()

q1=np.quantile(df3["LiabilitiesTotal"],0.25)
q3=np.quantile(df3["LiabilitiesTotal"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['LiabilitiesTotal'])):
    if df3['LiabilitiesTotal'][i]> max_bound:
        df3['LiabilitiesTotal'][i]=max_bound

sns.boxplot(df3['LiabilitiesTotal'],orient='h')
plt.show()

sns.boxplot(df3['DebtToIncome'],orient='h')
plt.show()

q1=np.quantile(df3["DebtToIncome"],0.25)
q3=np.quantile(df3["DebtToIncome"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['DebtToIncome'])):
    if df3['DebtToIncome'][i]> max_bound:
        df3['DebtToIncome'][i]=max_bound

sns.boxplot(df3['DebtToIncome'],orient='h')
plt.show()

sns.boxplot(df3['FreeCash'],orient='h')
plt.show()

q1=np.quantile(df3["FreeCash"],0.25)
q3=np.quantile(df3["FreeCash"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['FreeCash'])):
    if df3['FreeCash'][i]> max_bound:
        df3['FreeCash'][i]=max_bound

sns.boxplot(df3['FreeCash'],orient='h')
plt.show()

sns.boxplot(df3['PlannedInterestTillDate'],orient='h')
plt.show()

q1=np.quantile(df3["PlannedInterestTillDate"],0.25)
q3=np.quantile(df3["PlannedInterestTillDate"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['PlannedInterestTillDate'])):
    if df3['PlannedInterestTillDate'][i]> max_bound:
        df3['PlannedInterestTillDate'][i]=max_bound

sns.boxplot(df3['PlannedInterestTillDate'],orient='h')

plt.show()

sns.boxplot(df3['ExpectedReturn'],orient='h')
plt.show()

q1=np.quantile(df3["ExpectedReturn"],0.25)
q3=np.quantile(df3["ExpectedReturn"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['ExpectedReturn'])):
    if df3['ExpectedReturn'][i]> max_bound:
        df3['ExpectedReturn'][i]=max_bound
        
    elif df3['ExpectedReturn'][i]< min_bound:
        df3['ExpectedReturn'][i]=min_bound

sns.boxplot(df3['ExpectedReturn'],orient='h')
plt.show()

sns.boxplot(df3['PrincipalOverdueBySchedule'],orient='h')
plt.show()

q1=np.quantile(df3["PrincipalOverdueBySchedule"],0.25)
q3=np.quantile(df3["PrincipalOverdueBySchedule"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['PrincipalOverdueBySchedule'])):
    if df3['PrincipalOverdueBySchedule'][i]> max_bound:
        df3['PrincipalOverdueBySchedule'][i]=max_bound
    elif df3['PrincipalOverdueBySchedule'][i]< min_bound:
        df3['PrincipalOverdueBySchedule'][i]=min_bound

sns.boxplot(df3['PrincipalOverdueBySchedule'],orient='h')
plt.show()

# sns.boxplot(df3['PrincipalPaymentsMade'],orient='h')
# plt.show()

# q1=np.quantile(df3["PrincipalPaymentsMade"],0.25)
# q3=np.quantile(df3["PrincipalPaymentsMade"],0.75)
# IQR=q3-q1

# min_bound=q1-1.5*IQR
# max_bound=q3+1.5*IQR

# for i in range(len(df3['PrincipalPaymentsMade'])):
#     if df3['PrincipalPaymentsMade'][i]> max_bound:
#         df3['PrincipalPaymentsMade'][i]=max_bound

sns.boxplot(df3['PrincipalPaymentsMade'],orient='h')
plt.show()

sns.boxplot(df3['PrincipalBalance'],orient='h')
plt.show()

q1=np.quantile(df3["PrincipalBalance"],0.25)
q3=np.quantile(df3["PrincipalBalance"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['PrincipalBalance'])):
    if df3['PrincipalBalance'][i]> max_bound:
        df3['PrincipalBalance'][i]=max_bound

sns.boxplot(df3['PrincipalBalance'],orient='h')
plt.show()

sns.boxplot(df3['InterestAndPenaltyBalance'],orient='h')
plt.show()

q1=np.quantile(df3["InterestAndPenaltyBalance"],0.25)
q3=np.quantile(df3["InterestAndPenaltyBalance"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['InterestAndPenaltyBalance'])):
    if df3['InterestAndPenaltyBalance'][i]> max_bound:
        df3['InterestAndPenaltyBalance'][i]=max_bound

sns.boxplot(df3['InterestAndPenaltyBalance'],orient='h')
plt.show()

sns.boxplot(df3['AmountOfPreviousLoansBeforeLoan'],orient='h')
plt.show()

q1=np.quantile(df3["AmountOfPreviousLoansBeforeLoan"],0.25)
q3=np.quantile(df3["AmountOfPreviousLoansBeforeLoan"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['AmountOfPreviousLoansBeforeLoan'])):
    if df3['AmountOfPreviousLoansBeforeLoan'][i]> max_bound:
        df3['AmountOfPreviousLoansBeforeLoan'][i]=max_bound

sns.boxplot(df3['AmountOfPreviousLoansBeforeLoan'],orient='h')
plt.show()

sns.boxplot(df3['PreviousRepaymentsBeforeLoan'],orient='h')
plt.show()

q1=np.quantile(df3["PreviousRepaymentsBeforeLoan"],0.25)
q3=np.quantile(df3["PreviousRepaymentsBeforeLoan"],0.75)
IQR=q3-q1

min_bound=q1-1.5*IQR
max_bound=q3+1.5*IQR

for i in range(len(df3['PreviousRepaymentsBeforeLoan'])):
    if df3['PreviousRepaymentsBeforeLoan'][i]> max_bound:
        df3['PreviousRepaymentsBeforeLoan'][i]=max_bound

sns.boxplot(df3['PreviousRepaymentsBeforeLoan'],orient='h')
plt.show()

### 1.Label encoding

df3

NewCreditCustomer_encode = LabelEncoder()
df3['NewCreditCustomer'] = NewCreditCustomer_encode.fit_transform(df3['NewCreditCustomer'])
# false-0  ,  true- 1

df3

Restructured_encode = LabelEncoder()
df3['Restructured'] = Restructured_encode.fit_transform(df3['Restructured'])
# false-0  ,  true- 1

DefaultStatus_encode = LabelEncoder()
df3['DefaultStatus'] = DefaultStatus_encode.fit_transform(df3['DefaultStatus'])
# default-0  , not default-1

df3

# df3['DefaultStatus'] = df3['DefaultStatus'].replace({'Not default':0,'Default':1})

df3['EmploymentDurationCurrentEmployer'] = df3['EmploymentDurationCurrentEmployer'].replace({'UpTo3Years':2, 'MoreThan5Years':4, 'UpTo4Years':1, 'UpTo2Years':2,
       'UpTo1Year':3, 'UpTo5Years':3, 'TrialPeriod':0, 'Other':1, 'Retiree':1})

df3['EmploymentDurationCurrentEmployer'].unique()

df3

df3['LanguageCode'] = df3['LanguageCode'].replace({1:3,3:2,2:1,4:3,6:3,22:0, 15:0,9:1,5:0,10:0,13:0,7:0,21:0})

df3['LanguageCode'].unique()

df3

df3= df3.drop(['Country', 'County', 'City', 'Rating','Status','WorseLateCategory','CreditScoreEsMicroL'],axis=1)
df3

standard = StandardScaler()
df3["Age"] = standard.fit_transform(df3[["Age"]])
df3["AppliedAmount"] = standard.fit_transform(df3[["AppliedAmount"]])
df3["Amount"] = standard.fit_transform(df3[["Amount"]])
df3["Interest"] = standard.fit_transform(df3[["Interest"]])
df3["MonthlyPayment"] = standard.fit_transform(df3[["MonthlyPayment"]])
df3["IncomeTotal"] = standard.fit_transform(df3[["IncomeTotal"]])
df3["LiabilitiesTotal"] = standard.fit_transform(df3[["LiabilitiesTotal"]])
df3["DebtToIncome"] = standard.fit_transform(df3[["DebtToIncome"]])
df3["FreeCash"] = standard.fit_transform(df3[["FreeCash"]])
df3["PlannedInterestTillDate"] = standard.fit_transform(df3[["PlannedInterestTillDate"]])
df3["ExpectedReturn"] = standard.fit_transform(df3[["ExpectedReturn"]])
df3["PrincipalOverdueBySchedule"] = standard.fit_transform(df3[["PrincipalOverdueBySchedule"]])
df3["PrincipalPaymentsMade"] = standard.fit_transform(df3[["PrincipalPaymentsMade"]])
df3["InterestAndPenaltyPaymentsMade"] = standard.fit_transform(df3[["InterestAndPenaltyPaymentsMade"]])
df3["PrincipalBalance"] = standard.fit_transform(df3[["PrincipalBalance"]])
df3["InterestAndPenaltyBalance"] = standard.fit_transform(df3[["InterestAndPenaltyBalance"]])
df3["AmountOfPreviousLoansBeforeLoan"] = standard.fit_transform(df3[["AmountOfPreviousLoansBeforeLoan"]])
df3["PreviousRepaymentsBeforeLoan"] = standard.fit_transform(df3[["PreviousRepaymentsBeforeLoan"]])

df3

plt.figure(figsize=(35,25))
fp=sns.heatmap(df3.corr(),annot=True)
fp

selected_features=[]
for i in df3:
    corr= df3[i].corr(df3['DefaultStatus'])
    if corr>=.2 or corr<=-0.17:
        selected_features.append(i)
selected_features

df_new= df3[selected_features]
df_new

plt.figure(figsize=(20,10))
sns.heatmap(df_new.corr(),annot=True)

# df_new =  df_new.drop("",axis=1)
# df_new

corrm = df_new.corr()
corrm

hc = [(i,j)
for i in corrm.columns
for j in corrm.columns
if i != j and abs(corrm[i][j])>.5]
    
print (hc)

for i in df_new:
    multico = []
    for j in df_new:
        corr = df_new[i].corr(df_new[j])
        if corr>0.5 and i!=j :
            multico.append(j)
    print(f"{i} : {multico}")

for i in df_new:
    # for j in range(len(df_new)):
        corr= df_new[i].corr(df_new['DefaultStatus'])
        if corr>0.5:
            print(f"{i} : {corr}")

corre ={}
for i in ('UseOfLoan',"MaritalStatus","EmploymentStatus","OccupationArea","DebtToIncome","PrincipalOverdueBySchedule"):
    corr = df_new[i].corr(df_new["DefaultStatus"])
    corre[i]=corr
corre

selected_final =["BidsPortfolioManager","LiabilitiesTotal","PlannedInterestTillDate","NextPaymentNr","Interest","PrincipalOverdueBySchedule","EmploymentStatus","DefaultStatus"]
df_final = df_new[selected_final]
df_final

x = df_final.drop('DefaultStatus',axis=1)
y = df_final['DefaultStatus']

x

y

# Splitting the data  into train and test data

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

x_train

y_train

x_test

knn = KNeighborsClassifier()
knn.fit(x_train,y_train)

y_pred_knn = knn.predict(x_test)

y_test

acc_knn = accuracy_score(y_pred_knn,y_test)
acc_knn

log = LogisticRegression()
log.fit(x_train,y_train)

y_pred_log = log.predict(x_test)

y_test

acc_log = accuracy_score(y_pred_log,y_test)
acc_log

dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)

y_pred_dt = dt.predict(x_test)

y_test

acc_dt = accuracy_score(y_pred_dt,y_test)
acc_dt

rd = RandomForestClassifier()
rd.fit(x_train,y_train)

y_pred_rd = rd.predict(x_test)

y_test

acc_rd = accuracy_score(y_pred_rd,y_test)
acc_rd

adab = AdaBoostClassifier()
adab.fit(x_train,y_train)

y_pred_adab = adab.predict(x_test)

y_test

acc_adab=accuracy_score(y_pred_adab,y_test)
acc_adab

confusion_matrix_knn = confusion_matrix(y_test,y_pred_knn)

confusion_matrix_knn

sns.heatmap(confusion_matrix_knn,annot=True)

from sklearn.metrics import ConfusionMatrixDisplay,confusion_matrix
cm = confusion_matrix(y_test,y_pred_knn) 
disp = ConfusionMatrixDisplay(confusion_matrix=cm) 
disp.plot(cmap='Blues')
plt.title('Confusion Matrix') 
plt.show()

precision_knn = precision_score(y_pred_knn,y_test)
precision_knn

## confusion matrix of logistic regression
confusion_matrix_log = confusion_matrix(y_test,y_pred_log)

confusion_matrix_log

sns.heatmap(confusion_matrix_log,annot=True)

from sklearn.metrics import ConfusionMatrixDisplay,confusion_matrix
cm = confusion_matrix(y_test,y_pred_log) 
disp = ConfusionMatrixDisplay(confusion_matrix=cm) 
disp.plot(cmap='Blues')
plt.title('Confusion Matrix') 
plt.show()

precision_log = precision_score(y_pred_log,y_test)
precision_log

## confusion martrix of decision tree regressor 
from sklearn.metrics import ConfusionMatrixDisplay,confusion_matrix
cm = confusion_matrix(y_test,y_pred_dt) 
disp = ConfusionMatrixDisplay(confusion_matrix=cm) 
disp.plot(cmap='Blues')
plt.title('Confusion Matrix') 
plt.show()

precision_dt = precision_score(y_pred_dt,y_test)
precision_dt

## confusion martrix of random forest  regressor 
from sklearn.metrics import ConfusionMatrixDisplay,confusion_matrix
cm = confusion_matrix(y_test,y_pred_rd) 

disp = ConfusionMatrixDisplay(confusion_matrix=cm) 
disp.plot(cmap='Blues')
plt.title('Confusion Matrix') 
plt.show()

precision_rd = precision_score(y_pred_rd,y_test)
precision_rd

## confusion martrix of ada boost regressor 
from sklearn.metrics import ConfusionMatrixDisplay,confusion_matrix
cm = confusion_matrix(y_test,y_pred_adab) 
disp = ConfusionMatrixDisplay(confusion_matrix=cm) 
disp.plot(cmap='Blues')
plt.title('Confusion Matrix') 
plt.show()

precision_adab = precision_score(y_pred_adab,y_test)
precision_adab

## Model validation
df_validation = pd.DataFrame({'Model':['KNN','Logistic Regression','Decision Tree Regressor','Random Forest Regressor','Adaboosting'],
                              'accuracy_score':[acc_knn,acc_log,acc_dt,acc_rd,acc_adab],
                              'precision_score':[precision_knn,precision_log,precision_dt,precision_rd,precision_adab]})
df_validation.set_index('Model',inplace=True)
df_validation.sort_values('accuracy_score',ascending=False)

df_final["DefaultStatus"].value_counts()

smote=SMOTE()
x_resample,y_resample=smote.fit_resample(x,y)

y.value_counts()

y_resample.value_counts()

x_resample = df_final.drop('DefaultStatus',axis=1)
y_resample = df_final['DefaultStatus']

x_resample

y_resample

# Splitting the data  into train and test data

x_train,x_test,y_train,y_test = train_test_split(x_resample,y_resample,test_size=0.2,random_state=42)

x_train

y_train

y_test

knn1 = KNeighborsClassifier()
knn1.fit(x_train,y_train)

y_pred_knn1 = knn1.predict(x_test)

y_test

acc_knn1 = accuracy_score(y_pred_knn1,y_test)
acc_knn1

log1 = LogisticRegression()
log1.fit(x_train,y_train)

y_pred_log1 = log1.predict(x_test)

y_test

acc_log1 = accuracy_score(y_pred_log1,y_test)
acc_log1

dt1 = DecisionTreeClassifier()
dt1.fit(x_train,y_train)

y_pred_dt1 = dt1.predict(x_test)

y_test

acc_dt1 = accuracy_score(y_pred_dt1,y_test)
acc_dt1

rd1 = RandomForestClassifier()
rd1.fit(x_train,y_train)

y_pred_rd1 = rd1.predict(x_test)

y_test

acc_rd1= accuracy_score(y_pred_rd1,y_test)
acc_rd1

adab1 = AdaBoostClassifier()
adab1.fit(x_train,y_train)

y_pred_adab1 = adab1.predict(x_test)

y_test

acc_adab1 = accuracy_score(y_pred_adab1,y_test)
acc_adab1

svc_model = SVC()
svc_model.fit(x_train,y_train)

y_pred_svc = svc_model.predict(x_test)

y_test

acc_svc = accuracy_score(y_pred_svc,y_test)
acc_svc

precision_knn1=precision_score(y_test,y_pred_knn1)
precision_knn1

precision_log1=precision_score(y_test,y_pred_log1)
precision_log1

precision_dt1=precision_score(y_test,y_pred_dt1)
precision_dt1

precision_rd1=precision_score(y_test,y_pred_rd1)
precision_rd1

precision_adab1=precision_score(y_test,y_pred_adab1)
precision_adab1

precision_svm1=precision_score(y_test,y_pred_svc)
precision_svm1

## Model validation
df_validation = pd.DataFrame({'Model':['KNN','Logistic Regression','Decision Tree Regressor','Random Forest Regressor','Adaboosting','SVM'],
                              'accuracy_score':[acc_knn1,acc_log1,acc_dt1,acc_rd1,acc_adab1,acc_svc],
                              'precision_score':[precision_knn1,precision_log1,precision_dt1,precision_rd1,precision_adab1,precision_svm1]})
df_validation.set_index('Model',inplace=True)
df_validation.sort_values('accuracy_score',ascending=False)

from sklearn.model_selection import KFold,cross_val_score

kf=KFold(n_splits=5,shuffle=True,random_state=42)
scores=cross_val_score(rd,x,y,cv=kf)

parameter_grid = {'n_neighbors':[5,7,9,11],
                  'weights':['uniform','distance'],
                  'metric':['euclidean','manhattan','minkowski']}
gridsearch = GridSearchCV(estimator = knn,param_grid = parameter_grid, cv= 5, scoring = 'accuracy')
gridsearch.fit(x_train,y_train)

grid_result = pd.DataFrame(gridsearch.cv_results_)
grid_result[['param_metric','param_n_neighbors','param_weights','mean_test_score']].iloc[0:15]

print('Best Score')
gridsearch.best_score_

print('Best Parameters')
gridsearch.best_params_

BidsPortfolioManager","LiabilitiesTotal","PlannedInterestTillDate","NextPaymentNr",
"Interest","PrincipalOverdueBySchedule","EmploymentStatus","DefaultStatus"]

def Default_Status_Predictor(BidsPortfolioManager,LiabilitiesTotal,PlannedInterestTillDate,NextPaymentNr,Interest,PrincipalOverdueBySchedule,EmploymentStatus,DefaultStatus):