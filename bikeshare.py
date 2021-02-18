import time
import pandas as pd
import numpy as  np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns: 
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
        #  geting user input for city (chicago, new york city, washington:Using a while loop to handle invalid inputs).
    while True:
          city=input("Choose City to be Analysed : Chicago, New york City,Washington \n").lower().strip()
          if city not in["chicago" ,"new york city" , "washington"]:
            print("please enter the right city correctly ,chick then try again")
         
          else:
            print(f"{city} Chosen")
            break
      
    #  getting user input for month (all, january, february, ... , june)
    while True:
        month=input("\nchoose month to be analayzed for:'january','february','march','april','may','june' ,or type all if no month\n").lower().strip()
        if month not in['january', 'february', 'march', 'april', 'may', 'june','all']:
           print("please enter the right month correctly ,chick then try again")
           continue
        elif month!="all":  
           print(f"{month} chosen")
        else:
           print("no month filter")
        break
    
        
            # getting user input for day of week (all, monday, tuesday, ... sunday)
            #Using a while loop to handeling invalid inputs.and multiple if else  
    while True:
           day=input("\nchoose Day to be Analysed:Sunday,Monday,Tuesday...,7 or type all if no day , \n").title().strip()
           #making sure the user enters the "day correctly"
           if day not in['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday','All']:
              print("please enter the right day correctly ,chick then try again")
              continue
           elif day!="All":
              print(f"{day} chosen")
           else:
                print("no day filter")
           break
       


    print('-'*40)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    
    
    
    df=pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    #use pd.to_datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month ,day,hour from the Start Time column to create month,day,hour columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    
    # filtering by month if applicable/if month (specified)
    if month!= "all":
        # useing the index of the months list to get the corresponding int
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1
        # filtering by month to create the new dataframe
       df = df[df['month'] == month]
    
         
     
                
        
    
    # filtering by day of week if applicable/if day (specified)
    if day!="All":  
       # filtering by day of week to create the new dataframe
       df = df[df['day']==day.title()]
        
      
    return df


def time_stats(df):
    """Dtime_ss statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
 
    
    #  displaying the most common month
  
    common_month=df['month'].mode()[0]
   
       
      
    print(f"most common month is: ",common_month)

    # displaying the most common day of week
    common_day= df['day'].mode()[0]
    print ("Most common day of week:",common_day)
    #displaying the most common start hour
    most_common_hour= df['hour'].mode()[0]
    print('Most Popular Start Hour:',most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
       
 

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # displaying the most commonly used start station

  
    popular_Start_Station =df['Start Station'].mode()[0]
    print('popular_Start_Station: ',popular_Start_Station)
    # displaying the most commonly used end station
    
    popular_End_Station =df['End Station'].mode()[0]
    print('popular_End_Station: ',popular_End_Station)
    #  displaying the most frequent combination of start station and end station trip
    StrtEndcombi=(popular_Start_Station + popular_End_Station)
    print("frequent combination of start station and end station trip: ",StrtEndcombi)

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n') 
    start_time = time.time()

    #  display the total travel time
    sum_trip_duration=df['Trip Duration'].sum()
    print("total travel time: ",sum_trip_duration)

    # display the mean travel time
    mean_trip_duration=df['Trip Duration'].mean()
    print("mean travel time: ",mean_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display the counts of user types
    print("Count of User Types ")
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    
    
   
      # display the counts of gender   
    #using the try & except  taking into consideration of data missing in (Washington) the Gender and Birth Year columns         
   
    try:
       print("\nCount of Genders")
       gender_count = df['Gender'].value_counts()
       print(gender_count)
 
        
      

       # display the earliest, most recent, and most common year of birth
  

       print("\nBirth Year Calculations")
       print(f"earliest bearth year: {df ['Birth Year'].max()}")
       print(f"most recent bearth year: {df['Birth Year'].min()}") 
       print(f"common bearth year: {df['Birth Year'].mode()}")  
    except:
       print("washington is not containing any Gender or birth year data")
        
       print("\nThis took %s seconds." % (time.time() - start_time))
        
       print('-'*40)

   
        
        
'''dfine main() function. it calls get_filters,load_data ,trip_duration_stats,user_stats
functions in turn.       
'''
def main():
    while True:
        #unpacking 
        city, month, day = get_filters()
        #loading the data 
        df = load_data(city, month, day)
        #calling functions
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
         
     
        #asking & getting the user input for printing 5 raws of raw data
        while True:
          rawi=input("\nwould you like to print some raw data? type yes or no.\n")
     
          if rawi=='yes':
             rawd= df.head(5)
             print(rawd)
           
        
          else:
                
               break
        
              
           
       #asking & getting the user input for restarting or quitting the program
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
             break


if __name__ == "__main__":
	main()
