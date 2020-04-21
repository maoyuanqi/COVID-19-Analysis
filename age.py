import pandas as pd
pd.set_option('display.max_columns', None)

#loads data
confirmed_us = pd.read_csv("/Users/maoyuanqi/Desktop/uchicago/age/time_series_covid19_confirmed_US.csv")
#only province_state * all others
confirmed_us_new = confirmed_us.loc[:,['Combined_Key','Country_Region']]
confirmed_us_new = pd.merge(confirmed_us_new,confirmed_us.iloc[:,11:],left_index=True,right_index=True)
confirmed_us_new = pd.melt(confirmed_us_new,id_vars=['Combined_Key','Country_Region'],var_name='Date',value_name='num_confirmed')
#print(confirmed_us_new)
#confirmed_us_new.to_csv("confirmed_us.csv")

#group by country
country_confirmed_us = confirmed_us_new.groupby(['Date'])['num_confirmed'].sum()

country_confirmed_us = pd.DataFrame(country_confirmed_us).reset_index()
country_confirmed_us['Date']= pd.to_datetime(country_confirmed_us['Date'])
country_confirmed_us = country_confirmed_us.sort_values("Date")

country_confirmed_us['rate'] = [0 for i in range(len(country_confirmed_us))]
#manipulate
for i in range(1,len(country_confirmed_us)):
    country_confirmed_us.iloc[i,2] =  (country_confirmed_us.iloc[i,1] - country_confirmed_us.iloc[i-1,1])*100 / country_confirmed_us.iloc[i-1,1]
# print(country_confirmed_us)




#dead


#loads data
death_us = pd.read_csv("/Users/maoyuanqi/Desktop/uchicago/age/time_series_covid19_deaths_US.csv")
#only province_state * all others
death_us_new = death_us.loc[:,['Combined_Key','Country_Region']]
death_us_new = pd.merge(death_us_new,death_us.iloc[:,12:],left_index=True,right_index=True)
death_us_new = pd.melt(death_us_new,id_vars=['Combined_Key','Country_Region'],var_name='Date',value_name='num_death')


# #group by country
country_death_us = death_us_new.groupby(['Date'])['num_death'].sum()

country_death_us = pd.DataFrame(country_death_us).reset_index()
country_death_us['Date']= pd.to_datetime(country_death_us['Date'])
country_death_us = country_death_us.sort_values("Date")

#manipulate

country_summary_us = pd.merge(country_confirmed_us,country_death_us,left_on='Date',right_on='Date')
country_summary_us['death_rate'] = country_summary_us['num_death']/country_summary_us['num_confirmed']
country_summary_us.to_csv("us_summary.csv")







pd.set_option('display.max_columns', None)

#loads data
confirmed_china = pd.read_csv("/Users/maoyuanqi/Desktop/uchicago/age/time_series_covid19_confirmed_global.csv")
confirmed_china = confirmed_china[confirmed_china['Country/Region'] == 'China']
# #only province_state * all others
# print(confirmed_china)
confirmed_china_new = confirmed_china.loc[:,['Province/State','Country/Region']]
confirmed_china_new = pd.merge(confirmed_china_new,confirmed_china.iloc[:,4:],left_index=True,right_index=True)
confirmed_china_new = pd.melt(confirmed_china_new,id_vars=['Province/State','Country/Region'],var_name='Date',value_name='num_confirmed')
#print(confirmed_china_new)
#confirmed_china_new.to_csv("confirmed_china.csv")
#
#group by country
country_confirmed_china = confirmed_china_new.groupby(['Date'])['num_confirmed'].sum()
#
country_confirmed_china = pd.DataFrame(country_confirmed_china).reset_index()
country_confirmed_china['Date']= pd.to_datetime(country_confirmed_china['Date'])
country_confirmed_china = country_confirmed_china.sort_values("Date")
#
country_confirmed_china['rate'] = [0 for i in range(len(country_confirmed_china))]
#manipulate
for i in range(1,len(country_confirmed_china)):
    country_confirmed_china.iloc[i,2] =  (country_confirmed_china.iloc[i,1] - country_confirmed_china.iloc[i-1,1])*100 / country_confirmed_china.iloc[i-1,1]
#print(country_confirmed_china)
#
#
#
#
#dead


#loads data
death_china = pd.read_csv("/Users/maoyuanqi/Desktop/uchicago/age/time_series_covid19_deaths_global.csv")
death_china = death_china[death_china['Country/Region'] == 'China']

death_china_new = death_china.loc[:,['Province/State','Country/Region']]
death_china_new = pd.merge(death_china_new,death_china.iloc[:,4:],left_index=True,right_index=True)
death_china_new = pd.melt(death_china_new,id_vars=['Province/State','Country/Region'],var_name='Date',value_name='num_death')


# #group by country
country_death_china = death_china_new.groupby(['Date'])['num_death'].sum()

country_death_china = pd.DataFrame(country_death_china).reset_index()
country_death_china['Date']= pd.to_datetime(country_death_china['Date'])
country_death_china = country_death_china.sort_values("Date")

#manipulate

country_summary_china = pd.merge(country_confirmed_china,country_death_china,left_on='Date',right_on='Date')
country_summary_china['death_rate'] = country_summary_china['num_death']/country_summary_china['num_confirmed']
print(country_summary_china)
country_summary_china.to_csv("chinese_summary.csv")
#
#
#
#
#
#

