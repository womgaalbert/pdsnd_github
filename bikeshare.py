# Update of my Bike Share project file
import time
import pandas as pd
import calendar
import matplotlib.pyplot as plt

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    class AlExceptionError (ValueError):
            def __str__(self):
                return   ''
    city = input('Would you like to see data for Chicago, New York City or Washington : ... ').lower()

    while (True):
        try:
            # city = input('Would you like to see data for Chicago, New York City or Washington : ... ').lower()
        
            if  (city not in ['chicago','new york city','washington']):
                raise AlExceptionError
        except AlExceptionError:
             city = input('The Name of the city should be choising among the following: Chicago, New York City or Washington, try again :... ').lower()      
        else :
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Would you like to filter for which month (all, january, february, ... , june) ?   ').lower()
    while (True):
        try:
            if  (month not in ['all', 'january', 'february','march','april','may','june']):
                raise AlExceptionError
        except AlExceptionError:
            month = input('Your answer should be chosen among the following: all, january, february,march,april,may,june, try again :... ').lower()     
        else :
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = int(input('Would you like to filter for which day of the week (e.g : 0=Monday, 1=Tuesday...) ?   '))
    while (True):
        try:
            if  day not in range(0,8):
                raise ValueError
        except ValueError :
            day = int(input('Your answer should be an integer chosen among the following: 0=Monday, 1=Tuesday, 2=Wenesday,3=Thursday, 4=Friday, 5=Sarturday,6=Sunday,7=all, try again :... '))     
        else :
            break
    #print('The chosen city, month and day are the following :\n City: {} ,\n Month:{} ,\n Day: {} '.format(city, month, calendar.day_name[day]))
    
    return city, month, day


    print('-'*40)
      

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day < 7:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    return df

def display_data(df):
    view_data = input('\n Would you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data.lower()=='yes'):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
    print('-'*40)
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    #common_month1 = df['month'].value_counts().index[0][0]
    print('The most common month of Travel is:{}'. format(common_month))

    # TO DO: display the most common day of week
    common_day_week = calendar.day_name[df['day_of_week'].mode()[0]]

    print('The most common day of the week of Travel  is:', common_day_week)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    common_hour = df['hour'].mode()[0]

    print('The most common Start Hour of Travel is:', common_hour)
    
    # TO DO : VISUALIZATION OF Start Time Serie
    series = df['Start Time']
    series.hist()
    plt.title ('Histogram of the distribution of start time ')
    plt.show()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()
    #common_start_station1 = df['Start Station'].value_counts().index[0][0]
    print('\n The most commonly used start station of trip is :{} '.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()
    print('\n The most commonly used end station of trip is :', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = df['Start Station'][df['Start Station']==df['End Station']].mode()
    print('\n The most commonly used end station of trip is :', common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = sum(df['Trip Duration'])
    print('\nThe total travel time is :', total_travel)

    # TO DO: display mean travel time
    mean_travel = total_travel/len(df['Trip Duration'])
    print('\nThe average travel time is :', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try: 
        print( ' Here we the counts of Gender :\n', df['Gender'].value_counts())
         # TO DO : VISUALIZATION OF Gender
        fig = plt.figure()
        ax=fig.add_axes([0,0,1,1])
        gender = ['Men','Women']
        Number_per_gender = [df['Gender'].value_counts()[0],df['Gender'].value_counts()[1]]
        ax.bar(gender,Number_per_gender )
        ax.set_ylabel('Number of people per gender')
        ax.set_xlabel('Gender')
        plt.title ('Distribution of the population according to gender.')
        plt.show()
    except KeyError:
       print ('Gender Statistic non - applicable.\n')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\n Descriptif Statistics of Birth Year: \n', df['Birth Year'].describe())
        e   = df['Birth Year'].min() 
        res = df['Birth Year'].max() 
        co  = df['Birth Year'].mode()
        print('\n The earliest year of birth is: {} , \n the most recent year of birth is: {}\n and the most common year of birth: {} \n'.format(e,res,co) )
        # TO DO : VISUALIZATION OF Birth Year
        Birth_Year = df['Birth Year']
        Birth_Year.hist()
        plt.title ('Histogram of the distribution of Birth Year ')
        plt.show()
    
    except KeyError:
       print ('\n Birth Statistic non - applicable.')
      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

""" Useful links  and guides for the job done...
https://www.datasciencemadesimple.com/get-day-of-week-pandas-python-2/
https://www.python-course.eu/python3_exception_handling.php
https://www.codegrepper.com/code-examples/python/calculate+time+duration+python
https://youtu.be/-4tA5PAH9uU 
https://plotly.com/python/"""