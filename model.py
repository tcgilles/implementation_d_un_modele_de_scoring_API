# library imports
import joblib
import numpy as np
from pydantic import BaseModel
from typing import Union


# Class that describes the customer data
class CustomerData(BaseModel):
    CODE_GENDER: int
    FLAG_OWN_CAR: int
    FLAG_OWN_REALTY: int
    CNT_CHILDREN: int
    AMT_INCOME_TOTAL: Union[float, str]
    AMT_CREDIT: Union[float, str]
    REGION_POPULATION_RELATIVE: Union[float, str]
    DAYS_BIRTH: int
    DAYS_EMPLOYED: Union[float, str]
    DAYS_REGISTRATION: Union[float, str]
    DAYS_ID_PUBLISH: int
    OWN_CAR_AGE: Union[float, str]
    REGION_RATING_CLIENT: int
    REG_CITY_NOT_LIVE_CITY: int
    REG_CITY_NOT_WORK_CITY: int
    EXT_SOURCE_1: Union[float, str]
    EXT_SOURCE_2: Union[float, str]
    EXT_SOURCE_3: Union[float, str]
    OBS_30_CNT_SOCIAL_CIRCLE: Union[float, str]
    DEF_30_CNT_SOCIAL_CIRCLE: Union[float, str]
    NEW_DAYS_EMPLOYED_PERC: Union[float, str]
    NEW_INCOME_CREDIT_PERC: Union[float, str]
    NEW_INCOME_PER_PERSON: Union[float, str]
    NEW_ANNUITY_INCOME_PERC: Union[float, str]
    NEW_PAYMENT_RATE: Union[float, str]
    NEW_LOAN_VALUE_RATIO: Union[float, str]
    NEW_INCOME_PER_PERSON_PERC_AMT_ANNUITY: Union[float, str]
    NEW_INCOME_PER_PERSON_PERC_PAYMENT_RATE_INCOME_PER_PERSON: Union[float, str]
    NEW_FLAG_CREDIT_MORE_THAN_GOODSPRICE: Union[float, str]
    NEW_AGE_RANGE: int
    NEW_WORKING_YEAR_RANGE: Union[float, str]
    NEW_TOTAL_CONTACT_INFORMATION: int
    NEW_YEAR_LAST_PHONE_CHANGE: Union[float, str]
    NEW_MISS_DOCUMENTS_20: int
    NEW_FLAG_MISS_DOCUMENTS: int
    NEW_AMT_REQ_CREDIT_BUREAU_YEAR: Union[float, str]
    NAME_CONTRACT_TYPE_Cashloans: int
    NAME_CONTRACT_TYPE_Revolvingloans: int
    NAME_TYPE_SUITE_Children: int
    NAME_TYPE_SUITE_Family: int
    NAME_TYPE_SUITE_Groupofpeople: int
    NAME_TYPE_SUITE_Other_A: int
    NAME_TYPE_SUITE_Other_B: int
    NAME_TYPE_SUITE_Spousepartner: int
    NAME_TYPE_SUITE_Unaccompanied: int
    NAME_TYPE_SUITE_nan: int
    NAME_EDUCATION_TYPE_Academicdegree: int
    NAME_EDUCATION_TYPE_Highereducation: int
    NAME_EDUCATION_TYPE_Incompletehigher: int
    NAME_EDUCATION_TYPE_Lowersecondary: int
    NAME_EDUCATION_TYPE_Secondarysecondaryspecial: int
    NAME_FAMILY_STATUS_Civilmarriage: int
    NAME_FAMILY_STATUS_Married: int
    NAME_FAMILY_STATUS_Separated: int
    NAME_FAMILY_STATUS_Singlenotmarried: int
    NAME_FAMILY_STATUS_Widow: int
    NAME_HOUSING_TYPE_Coopapartment: int
    NAME_HOUSING_TYPE_Houseapartment: int
    NAME_HOUSING_TYPE_Municipalapartment: int
    NAME_HOUSING_TYPE_Officeapartment: int
    NAME_HOUSING_TYPE_Rentedapartment: int
    NAME_HOUSING_TYPE_Withparents: int
    OCCUPATION_TYPE_Accountants: int
    OCCUPATION_TYPE_Cleaningstaff: int
    OCCUPATION_TYPE_Cookingstaff: int
    OCCUPATION_TYPE_Corestaff: int
    OCCUPATION_TYPE_Drivers: int
    OCCUPATION_TYPE_HRstaff: int
    OCCUPATION_TYPE_Highskilltechstaff: int
    OCCUPATION_TYPE_ITstaff: int
    OCCUPATION_TYPE_Laborers: int
    OCCUPATION_TYPE_LowskillLaborers: int
    OCCUPATION_TYPE_Managers: int
    OCCUPATION_TYPE_Medicinestaff: int
    OCCUPATION_TYPE_Privateservicestaff: int
    OCCUPATION_TYPE_Realtyagents: int
    OCCUPATION_TYPE_Salesstaff: int
    OCCUPATION_TYPE_Secretaries: int
    OCCUPATION_TYPE_Securitystaff: int
    OCCUPATION_TYPE_Waitersbarmenstaff: int
    OCCUPATION_TYPE_nan: int
    BURO_DAYS_CREDIT_MIN: Union[float, str]
    BURO_DAYS_CREDIT_MAX: Union[float, str]
    BURO_DAYS_CREDIT_MEAN: Union[float, str]
    BURO_DAYS_CREDIT_VAR: Union[float, str]
    BURO_DAYS_CREDIT_ENDDATE_MIN: Union[float, str]
    BURO_DAYS_CREDIT_ENDDATE_MAX: Union[float, str]
    BURO_DAYS_CREDIT_ENDDATE_MEAN: Union[float, str]
    BURO_CREDIT_DAY_OVERDUE_MAX: Union[float, str]
    BURO_CREDIT_DAY_OVERDUE_MEAN: Union[float, str]
    BURO_AMT_CREDIT_MAX_OVERDUE_MEAN: Union[float, str]
    BURO_AMT_CREDIT_SUM_MAX: Union[float, str]
    BURO_AMT_CREDIT_SUM_MEAN: Union[float, str]
    BURO_AMT_CREDIT_SUM_SUM: Union[float, str]
    BURO_AMT_CREDIT_SUM_OVERDUE_MEAN: Union[float, str]
    BURO_AMT_CREDIT_SUM_LIMIT_MEAN: Union[float, str]
    BURO_AMT_CREDIT_SUM_LIMIT_SUM: Union[float, str]
    BURO_AMT_ANNUITY_MAX: Union[float, str]
    BURO_AMT_ANNUITY_MEAN: Union[float, str]
    BURO_CNT_CREDIT_PROLONG_SUM: Union[float, str]
    BURO_BB_MONTHS_BALANCE_MIN_MIN: Union[float, str]
    BURO_BB_MONTHS_BALANCE_MAX_MAX: Union[float, str]
    BURO_BB_MONTHS_BALANCE_SIZE_MEAN: Union[float, str]
    BURO_BB_MONTHS_BALANCE_SIZE_SUM: Union[float, str]
    BURO_NEW_BUREAU_LOAN_COUNT_MEAN: Union[float, str]
    BURO_NEW_BUREAU_LOAN_TYPES_MEAN: Union[float, str]
    BURO_NEW_ACTIVE_LOANS_PERCENTAGE_MAX: Union[float, str]
    BURO_NEW_ACTIVE_LOANS_PERCENTAGE_MEAN: Union[float, str]
    BURO_NEW_CREDIT_ENDDATE_PERCENTAGE_MAX: Union[float, str]
    BURO_NEW_CREDIT_ENDDATE_PERCENTAGE_MEAN: Union[float, str]
    BURO_NEW_DEBT_CREDIT_RATIO_MAX: Union[float, str]
    BURO_NEW_DEBT_CREDIT_RATIO_MEAN: Union[float, str]
    BURO_CREDIT_ACTIVE_Active_MEAN: Union[float, str]
    BURO_CREDIT_ACTIVE_Closed_MEAN: Union[float, str]
    BURO_CREDIT_ACTIVE_Rare_MEAN: Union[float, str]
    BURO_CREDIT_CURRENCY_Rare_MEAN: Union[float, str]
    BURO_CREDIT_CURRENCY_currency1_MEAN: Union[float, str]
    BURO_CREDIT_TYPE_Carloan_MEAN: Union[float, str]
    BURO_CREDIT_TYPE_Consumercredit_MEAN: Union[float, str]
    BURO_CREDIT_TYPE_Creditcard_MEAN: Union[float, str]
    BURO_CREDIT_TYPE_Mortgage_MEAN: Union[float, str]
    BURO_CREDIT_TYPE_Rare_MEAN: Union[float, str]
    BURO_BB_STATUS_0_MEAN_MEAN: Union[float, str]
    BURO_BB_STATUS_1_MEAN_MEAN: Union[float, str]
    BURO_BB_STATUS_2_MEAN_MEAN: Union[float, str]
    BURO_BB_STATUS_3_MEAN_MEAN: Union[float, str]
    BURO_BB_STATUS_4_MEAN_MEAN: Union[float, str]
    BURO_BB_STATUS_5_MEAN_MEAN: Union[float, str]
    BURO_BB_STATUS_C_MEAN_MEAN: Union[float, str]
    BURO_BB_STATUS_X_MEAN_MEAN: Union[float, str]
    ACTIVE_DAYS_CREDIT_MIN: Union[float, str]
    ACTIVE_DAYS_CREDIT_MAX: Union[float, str]
    ACTIVE_DAYS_CREDIT_MEAN: Union[float, str]
    ACTIVE_DAYS_CREDIT_VAR: Union[float, str]
    ACTIVE_DAYS_CREDIT_ENDDATE_MIN: Union[float, str]
    ACTIVE_DAYS_CREDIT_ENDDATE_MAX: Union[float, str]
    ACTIVE_DAYS_CREDIT_ENDDATE_MEAN: Union[float, str]
    ACTIVE_CREDIT_DAY_OVERDUE_MAX: Union[float, str]
    ACTIVE_CREDIT_DAY_OVERDUE_MEAN: Union[float, str]
    ACTIVE_AMT_CREDIT_MAX_OVERDUE_MEAN: Union[float, str]
    ACTIVE_AMT_CREDIT_SUM_MAX: Union[float, str]
    ACTIVE_AMT_CREDIT_SUM_MEAN: Union[float, str]
    ACTIVE_AMT_CREDIT_SUM_SUM: Union[float, str]
    ACTIVE_AMT_CREDIT_SUM_OVERDUE_MEAN: Union[float, str]
    ACTIVE_AMT_CREDIT_SUM_LIMIT_MEAN: Union[float, str]
    ACTIVE_AMT_CREDIT_SUM_LIMIT_SUM: Union[float, str]
    ACTIVE_AMT_ANNUITY_MAX: Union[float, str]
    ACTIVE_AMT_ANNUITY_MEAN: Union[float, str]
    ACTIVE_CNT_CREDIT_PROLONG_SUM: Union[float, str]
    ACTIVE_BB_MONTHS_BALANCE_MIN_MIN: Union[float, str]
    ACTIVE_BB_MONTHS_BALANCE_MAX_MAX: Union[float, str]
    ACTIVE_BB_MONTHS_BALANCE_SIZE_MEAN: Union[float, str]
    ACTIVE_BB_MONTHS_BALANCE_SIZE_SUM: Union[float, str]
    ACTIVE_NEW_BUREAU_LOAN_COUNT_MEAN: Union[float, str]
    ACTIVE_NEW_BUREAU_LOAN_TYPES_MEAN: Union[float, str]
    ACTIVE_NEW_ACTIVE_LOANS_PERCENTAGE_MAX: Union[float, str]
    ACTIVE_NEW_ACTIVE_LOANS_PERCENTAGE_MEAN: Union[float, str]
    ACTIVE_NEW_CREDIT_ENDDATE_PERCENTAGE_MAX: Union[float, str]
    ACTIVE_NEW_CREDIT_ENDDATE_PERCENTAGE_MEAN: Union[float, str]
    ACTIVE_NEW_DEBT_CREDIT_RATIO_MAX: Union[float, str]
    ACTIVE_NEW_DEBT_CREDIT_RATIO_MEAN: Union[float, str]
    CLOSED_DAYS_CREDIT_MIN: Union[float, str]
    CLOSED_DAYS_CREDIT_MAX: Union[float, str]
    CLOSED_DAYS_CREDIT_MEAN: Union[float, str]
    CLOSED_DAYS_CREDIT_VAR: Union[float, str]
    CLOSED_DAYS_CREDIT_ENDDATE_MIN: Union[float, str]
    CLOSED_DAYS_CREDIT_ENDDATE_MAX: Union[float, str]
    CLOSED_DAYS_CREDIT_ENDDATE_MEAN: Union[float, str]
    CLOSED_CREDIT_DAY_OVERDUE_MAX: Union[float, str]
    CLOSED_CREDIT_DAY_OVERDUE_MEAN: Union[float, str]
    CLOSED_AMT_CREDIT_MAX_OVERDUE_MEAN: Union[float, str]
    CLOSED_AMT_CREDIT_SUM_MAX: Union[float, str]
    CLOSED_AMT_CREDIT_SUM_MEAN: Union[float, str]
    CLOSED_AMT_CREDIT_SUM_SUM: Union[float, str]
    CLOSED_AMT_CREDIT_SUM_OVERDUE_MEAN: Union[float, str]
    CLOSED_AMT_CREDIT_SUM_LIMIT_MEAN: Union[float, str]
    CLOSED_AMT_CREDIT_SUM_LIMIT_SUM: Union[float, str]
    CLOSED_AMT_ANNUITY_MAX: Union[float, str]
    CLOSED_AMT_ANNUITY_MEAN: Union[float, str]
    CLOSED_CNT_CREDIT_PROLONG_SUM: Union[float, str]
    CLOSED_BB_MONTHS_BALANCE_MIN_MIN: Union[float, str]
    CLOSED_BB_MONTHS_BALANCE_MAX_MAX: Union[float, str]
    CLOSED_BB_MONTHS_BALANCE_SIZE_MEAN: Union[float, str]
    CLOSED_BB_MONTHS_BALANCE_SIZE_SUM: Union[float, str]
    CLOSED_NEW_BUREAU_LOAN_COUNT_MEAN: Union[float, str]
    CLOSED_NEW_BUREAU_LOAN_TYPES_MEAN: Union[float, str]
    CLOSED_NEW_ACTIVE_LOANS_PERCENTAGE_MAX: Union[float, str]
    CLOSED_NEW_ACTIVE_LOANS_PERCENTAGE_MEAN: Union[float, str]
    CLOSED_NEW_CREDIT_ENDDATE_PERCENTAGE_MAX: Union[float, str]
    CLOSED_NEW_CREDIT_ENDDATE_PERCENTAGE_MEAN: Union[float, str]
    CLOSED_NEW_DEBT_CREDIT_RATIO_MAX: Union[float, str]
    CLOSED_NEW_DEBT_CREDIT_RATIO_MEAN: Union[float, str]
    PREV_SK_ID_PREV_COUNT: Union[float, str]
    PREV_AMT_APPLICATION_MIN: Union[float, str]
    PREV_AMT_APPLICATION_MAX: Union[float, str]
    PREV_AMT_APPLICATION_MEAN: Union[float, str]
    PREV_AMT_APPLICATION_MEDIAN: Union[float, str]
    PREV_RATE_DOWN_PAYMENT_MIN: Union[float, str]
    PREV_RATE_DOWN_PAYMENT_MAX: Union[float, str]
    PREV_RATE_DOWN_PAYMENT_MEAN: Union[float, str]
    PREV_RATE_DOWN_PAYMENT_MEDIAN: Union[float, str]
    PREV_DAYS_DECISION_MIN: Union[float, str]
    PREV_DAYS_DECISION_MAX: Union[float, str]
    PREV_DAYS_DECISION_MEAN: Union[float, str]
    PREV_DAYS_DECISION_MEDIAN: Union[float, str]
    PREV_NEW_RETURN_DAY_MIN: Union[float, str]
    PREV_NEW_RETURN_DAY_MAX: Union[float, str]
    PREV_NEW_RETURN_DAY_MEAN: Union[float, str]
    PREV_NEW_RETURN_DAY_VAR: Union[float, str]
    PREV_NEW_DAYS_TERMINATION_DIFF_MIN: Union[float, str]
    PREV_NEW_DAYS_TERMINATION_DIFF_MAX: Union[float, str]
    PREV_NEW_DAYS_TERMINATION_DIFF_MEAN: Union[float, str]
    PREV_NEW_DAYS_DUE_DIFF_MIN: Union[float, str]
    PREV_NEW_DAYS_DUE_DIFF_MAX: Union[float, str]
    PREV_NEW_DAYS_DUE_DIFF_MEAN: Union[float, str]
    PREV_WEEKDAY_APPR_PROCESS_START_WEEKDAY_MEAN: Union[float, str]
    PREV_WEEKDAY_APPR_PROCESS_START_WEEKEND_MEAN: Union[float, str]
    PREV_FLAG_LAST_APPL_PER_CONTRACT_N_MEAN: Union[float, str]
    PREV_FLAG_LAST_APPL_PER_CONTRACT_Y_MEAN: Union[float, str]
    PREV_NFLAG_LAST_APPL_IN_DAY_00_MEAN: Union[float, str]
    PREV_NFLAG_LAST_APPL_IN_DAY_10_MEAN: Union[float, str]
    PREV_NAME_PAYMENT_TYPE_Cashthroughthebank_MEAN: Union[float, str]
    PREV_NAME_PAYMENT_TYPE_Cashlessfromtheaccountoftheemployer_MEAN: Union[float, str]
    PREV_NAME_PAYMENT_TYPE_Noncashfromyouraccount_MEAN: Union[float, str]
    PREV_NAME_PAYMENT_TYPE_XNA_MEAN: Union[float, str]
    PREV_NAME_TYPE_SUITE_Accompanied_MEAN: Union[float, str]
    PREV_NAME_TYPE_SUITE_Unaccompanied_MEAN: Union[float, str]
    PREV_NAME_TYPE_SUITE_nan_MEAN: Union[float, str]
    PREV_NAME_CLIENT_TYPE_New_MEAN: Union[float, str]
    PREV_NAME_CLIENT_TYPE_Refreshed_MEAN: Union[float, str]
    PREV_NAME_CLIENT_TYPE_Repeater_MEAN: Union[float, str]
    PREV_NAME_CLIENT_TYPE_XNA_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_CardStreet_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_CardXSell_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_Cash_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_CashStreethigh_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_CashStreetlow_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_CashStreetmiddle_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_CashXSellhigh_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_CashXSelllow_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_CashXSellmiddle_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_POShouseholdwithinterest_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_POShouseholdwithoutinterest_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_POSindustrywithinterest_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_POSindustrywithoutinterest_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_POSmobilewithinterest_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_POSmobilewithoutinterest_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_POSotherwithinterest_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_POSotherswithoutinterest_MEAN: Union[float, str]
    PREV_PRODUCT_COMBINATION_nan_MEAN: Union[float, str]
    POS_MONTHS_BALANCE_MAX: Union[float, str]
    POS_MONTHS_BALANCE_MEAN: Union[float, str]
    POS_MONTHS_BALANCE_SIZE: Union[float, str]
    POS_SK_DPD_MAX: Union[float, str]
    POS_SK_DPD_MEAN: Union[float, str]
    POS_SK_DPD_DEF_MAX: Union[float, str]
    POS_SK_DPD_DEF_MEAN: Union[float, str]
    POS_NAME_CONTRACT_STATUS_Active_MEAN: Union[float, str]
    POS_NAME_CONTRACT_STATUS_Amortizeddebt_MEAN: Union[float, str]
    POS_NAME_CONTRACT_STATUS_Approved_MEAN: Union[float, str]
    POS_NAME_CONTRACT_STATUS_Canceled_MEAN: Union[float, str]
    POS_NAME_CONTRACT_STATUS_Completed_MEAN: Union[float, str]
    POS_NAME_CONTRACT_STATUS_Demand_MEAN: Union[float, str]
    POS_NAME_CONTRACT_STATUS_Returnedtothestore_MEAN: Union[float, str]
    POS_NAME_CONTRACT_STATUS_Signed_MEAN: Union[float, str]
    POS_NAME_CONTRACT_STATUS_XNA_MEAN: Union[float, str]
    POS_COUNT: Union[float, str]
    INSTAL_NUM_INSTALMENT_VERSION_NUNIQUE: Union[float, str]
    INSTAL_DPD_MAX: Union[float, str]
    INSTAL_DPD_MEAN: Union[float, str]
    INSTAL_DPD_SUM: Union[float, str]
    INSTAL_DBD_MAX: Union[float, str]
    INSTAL_DBD_MEAN: Union[float, str]
    INSTAL_DBD_SUM: Union[float, str]
    INSTAL_PAYMENT_PERC_MAX: Union[float, str]
    INSTAL_PAYMENT_PERC_MEAN: Union[float, str]
    INSTAL_PAYMENT_PERC_SUM: Union[float, str]
    INSTAL_PAYMENT_PERC_VAR: Union[float, str]
    INSTAL_PAYMENT_DIFF_MAX: Union[float, str]
    INSTAL_PAYMENT_DIFF_MEAN: Union[float, str]
    INSTAL_PAYMENT_DIFF_SUM: Union[float, str]
    INSTAL_PAYMENT_DIFF_VAR: Union[float, str]
    INSTAL_AMT_INSTALMENT_MAX: Union[float, str]
    INSTAL_AMT_INSTALMENT_MEAN: Union[float, str]
    INSTAL_AMT_INSTALMENT_SUM: Union[float, str]
    INSTAL_AMT_PAYMENT_MIN: Union[float, str]
    INSTAL_AMT_PAYMENT_MAX: Union[float, str]
    INSTAL_AMT_PAYMENT_MEAN: Union[float, str]
    INSTAL_AMT_PAYMENT_SUM: Union[float, str]
    INSTAL_DAYS_ENTRY_PAYMENT_MAX: Union[float, str]
    INSTAL_DAYS_ENTRY_PAYMENT_MEAN: Union[float, str]
    INSTAL_DAYS_ENTRY_PAYMENT_SUM: Union[float, str]
    INSTAL_COUNT: Union[float, str]
    CC_MONTHS_BALANCE_MIN: Union[float, str]
    CC_MONTHS_BALANCE_MAX: Union[float, str]
    CC_MONTHS_BALANCE_MEAN: Union[float, str]
    CC_MONTHS_BALANCE_SUM: Union[float, str]
    CC_MONTHS_BALANCE_VAR: Union[float, str]
    CC_AMT_BALANCE_MIN: Union[float, str]
    CC_AMT_BALANCE_MAX: Union[float, str]
    CC_AMT_BALANCE_MEAN: Union[float, str]
    CC_AMT_BALANCE_SUM: Union[float, str]
    CC_AMT_BALANCE_VAR: Union[float, str]
    CC_AMT_CREDIT_LIMIT_ACTUAL_MIN: Union[float, str]
    CC_AMT_CREDIT_LIMIT_ACTUAL_MAX: Union[float, str]
    CC_AMT_CREDIT_LIMIT_ACTUAL_MEAN: Union[float, str]
    CC_AMT_CREDIT_LIMIT_ACTUAL_SUM: Union[float, str]
    CC_AMT_CREDIT_LIMIT_ACTUAL_VAR: Union[float, str]
    CC_AMT_DRAWINGS_ATM_CURRENT_MIN: Union[float, str]
    CC_AMT_DRAWINGS_ATM_CURRENT_MAX: Union[float, str]
    CC_AMT_DRAWINGS_ATM_CURRENT_MEAN: Union[float, str]
    CC_AMT_DRAWINGS_ATM_CURRENT_SUM: Union[float, str]
    CC_AMT_DRAWINGS_ATM_CURRENT_VAR: Union[float, str]
    CC_AMT_DRAWINGS_CURRENT_MIN: Union[float, str]
    CC_AMT_DRAWINGS_CURRENT_MAX: Union[float, str]
    CC_AMT_DRAWINGS_CURRENT_MEAN: Union[float, str]
    CC_AMT_DRAWINGS_CURRENT_SUM: Union[float, str]
    CC_AMT_DRAWINGS_CURRENT_VAR: Union[float, str]
    CC_AMT_DRAWINGS_OTHER_CURRENT_MIN: Union[float, str]
    CC_AMT_DRAWINGS_OTHER_CURRENT_MAX: Union[float, str]
    CC_AMT_DRAWINGS_OTHER_CURRENT_MEAN: Union[float, str]
    CC_AMT_DRAWINGS_OTHER_CURRENT_SUM: Union[float, str]
    CC_AMT_DRAWINGS_OTHER_CURRENT_VAR: Union[float, str]
    CC_AMT_DRAWINGS_POS_CURRENT_MIN: Union[float, str]
    CC_AMT_DRAWINGS_POS_CURRENT_MAX: Union[float, str]
    CC_AMT_DRAWINGS_POS_CURRENT_MEAN: Union[float, str]
    CC_AMT_DRAWINGS_POS_CURRENT_SUM: Union[float, str]
    CC_AMT_DRAWINGS_POS_CURRENT_VAR: Union[float, str]
    CC_AMT_INST_MIN_REGULARITY_MIN: Union[float, str]
    CC_AMT_INST_MIN_REGULARITY_MAX: Union[float, str]
    CC_AMT_INST_MIN_REGULARITY_MEAN: Union[float, str]
    CC_AMT_INST_MIN_REGULARITY_SUM: Union[float, str]
    CC_AMT_INST_MIN_REGULARITY_VAR: Union[float, str]
    CC_AMT_PAYMENT_CURRENT_MIN: Union[float, str]
    CC_AMT_PAYMENT_CURRENT_MAX: Union[float, str]
    CC_AMT_PAYMENT_CURRENT_MEAN: Union[float, str]
    CC_AMT_PAYMENT_CURRENT_SUM: Union[float, str]
    CC_AMT_PAYMENT_CURRENT_VAR: Union[float, str]
    CC_AMT_PAYMENT_TOTAL_CURRENT_MIN: Union[float, str]
    CC_AMT_PAYMENT_TOTAL_CURRENT_MAX: Union[float, str]
    CC_AMT_PAYMENT_TOTAL_CURRENT_MEAN: Union[float, str]
    CC_AMT_PAYMENT_TOTAL_CURRENT_SUM: Union[float, str]
    CC_AMT_PAYMENT_TOTAL_CURRENT_VAR: Union[float, str]
    CC_AMT_RECEIVABLE_PRINCIPAL_MIN: Union[float, str]
    CC_AMT_RECEIVABLE_PRINCIPAL_MAX: Union[float, str]
    CC_AMT_RECEIVABLE_PRINCIPAL_MEAN: Union[float, str]
    CC_AMT_RECEIVABLE_PRINCIPAL_SUM: Union[float, str]
    CC_AMT_RECEIVABLE_PRINCIPAL_VAR: Union[float, str]
    CC_AMT_RECIVABLE_MIN: Union[float, str]
    CC_AMT_RECIVABLE_MAX: Union[float, str]
    CC_AMT_RECIVABLE_MEAN: Union[float, str]
    CC_AMT_RECIVABLE_SUM: Union[float, str]
    CC_AMT_RECIVABLE_VAR: Union[float, str]
    CC_AMT_TOTAL_RECEIVABLE_MIN: Union[float, str]
    CC_AMT_TOTAL_RECEIVABLE_MAX: Union[float, str]
    CC_AMT_TOTAL_RECEIVABLE_MEAN: Union[float, str]
    CC_AMT_TOTAL_RECEIVABLE_SUM: Union[float, str]
    CC_AMT_TOTAL_RECEIVABLE_VAR: Union[float, str]
    CC_CNT_DRAWINGS_ATM_CURRENT_MIN: Union[float, str]
    CC_CNT_DRAWINGS_ATM_CURRENT_MAX: Union[float, str]
    CC_CNT_DRAWINGS_ATM_CURRENT_MEAN: Union[float, str]
    CC_CNT_DRAWINGS_ATM_CURRENT_SUM: Union[float, str]
    CC_CNT_DRAWINGS_ATM_CURRENT_VAR: Union[float, str]
    CC_CNT_DRAWINGS_CURRENT_MIN: Union[float, str]
    CC_CNT_DRAWINGS_CURRENT_MAX: Union[float, str]
    CC_CNT_DRAWINGS_CURRENT_MEAN: Union[float, str]
    CC_CNT_DRAWINGS_CURRENT_SUM: Union[float, str]
    CC_CNT_DRAWINGS_CURRENT_VAR: Union[float, str]
    CC_CNT_DRAWINGS_OTHER_CURRENT_MIN: Union[float, str]
    CC_CNT_DRAWINGS_OTHER_CURRENT_MAX: Union[float, str]
    CC_CNT_DRAWINGS_OTHER_CURRENT_MEAN: Union[float, str]
    CC_CNT_DRAWINGS_OTHER_CURRENT_SUM: Union[float, str]
    CC_CNT_DRAWINGS_OTHER_CURRENT_VAR: Union[float, str]
    CC_CNT_DRAWINGS_POS_CURRENT_MIN: Union[float, str]
    CC_CNT_DRAWINGS_POS_CURRENT_MAX: Union[float, str]
    CC_CNT_DRAWINGS_POS_CURRENT_MEAN: Union[float, str]
    CC_CNT_DRAWINGS_POS_CURRENT_SUM: Union[float, str]
    CC_CNT_DRAWINGS_POS_CURRENT_VAR: Union[float, str]
    CC_CNT_INSTALMENT_MATURE_CUM_MIN: Union[float, str]
    CC_CNT_INSTALMENT_MATURE_CUM_MAX: Union[float, str]
    CC_CNT_INSTALMENT_MATURE_CUM_MEAN: Union[float, str]
    CC_CNT_INSTALMENT_MATURE_CUM_SUM: Union[float, str]
    CC_CNT_INSTALMENT_MATURE_CUM_VAR: Union[float, str]
    CC_SK_DPD_MAX: Union[float, str]
    CC_SK_DPD_MEAN: Union[float, str]
    CC_SK_DPD_SUM: Union[float, str]
    CC_SK_DPD_VAR: Union[float, str]
    CC_SK_DPD_DEF_MAX: Union[float, str]
    CC_SK_DPD_DEF_MEAN: Union[float, str]
    CC_SK_DPD_DEF_SUM: Union[float, str]
    CC_SK_DPD_DEF_VAR: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Active_MIN: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Active_MAX: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Active_MEAN: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Active_SUM: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Active_VAR: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Approved_MAX: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Approved_MEAN: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Approved_SUM: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Approved_VAR: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Completed_MIN: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Completed_MAX: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Completed_MEAN: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Completed_SUM: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Completed_VAR: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Demand_MAX: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Demand_MEAN: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Demand_SUM: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Demand_VAR: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Refused_MAX: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Refused_MEAN: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Refused_SUM: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Refused_VAR: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Sentproposal_MAX: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Sentproposal_MEAN: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Sentproposal_SUM: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Sentproposal_VAR: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Signed_MIN: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Signed_MAX: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Signed_MEAN: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Signed_SUM: Union[float, str]
    CC_NAME_CONTRACT_STATUS_Signed_VAR: Union[float, str]
    CC_COUNT: Union[float, str]


# class for makig predictions
class CreditModel:

    # Loads the model
    def __init__(self):
        self.model = joblib.load("model.pkl")

    # Make a prediction of defaulting based on the user-entered data
    def predict_score(self, customer_data:CustomerData):

        # transforms the object in a dictionnary
        data = customer_data.dict()

        # The missing values were encoded with a string character in
        # order to be valid JSON format. We decode them with this line.
        retrieve_nans = list(map(lambda x: float("nan") if 
                                 isinstance(x, str) else x, 
                                 data.values()))
        
        # We change the values of data to take into account the missing
        # values we've just retrieved.
        data = dict(zip(data.keys(), retrieve_nans))

        # We transform the dictionnary into a 2D numpy ndarray
        input_values = np.array(list(data.values())).reshape(1,-1)

        # We make the prediction with the model
        probability = self.model.predict_proba(input_values)

        # We only return the probability of class 1
        return probability[0,1]

    