import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New york city': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('Chicago', 'New york city', 'Washington')
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']

    while True:
        city = input('Which of these cities do you want to see data : {} \n'.format(cities))
        if city in cities:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter a month to get result {} \n'.format(months))
        if month in months:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)    
    while True:
        day = input('Please enter a day to get result {} \n'.format(days))
        if day in days:
            break
    print('-'*40)
#     print("city, month, day" + city, month, day)
    return city, month, day


def load_data(city, month, day):
   
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
     
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    print(day)
    print(month)

    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #TO DO: display the most common month      
    mostCommonMonth = df['month'].mode()[0]
    print("\nMost common month is ..", mostCommonMonth)
    

    # TO DO: display the most common day of week
    mostCommonDayOfWeek = df['day_of_week'].mode()[0]
    print("\nMost common day of week is ..", mostCommonDayOfWeek)

    
    # TO DO: display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    mostCommonStartHour = df['hour'].mode()[0]
    print("\nMost common start hour is ..", mostCommonStartHour)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mostCommonStartStation = df['Start Station'].value_counts().idxmax()
    print("\nMost commonly used start station is ..", mostCommonStartStation)

    # TO DO: display most commonly used end station
    mostCommonEndStation = df['End Station'].value_counts().idxmax()
    print("\nMost commonly used end station is ..", mostCommonEndStation)

    # TO DO: display most frequent combination of start station and end station trip
    mostCommonStartEndStation = df.groupby(['Start Station', 'End Station']).count()
    print("\nMost commonly used combination of start station and end station is .." ,mostCommonStartStation , " & ", mostCommonEndStation)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTravel = df['Trip Duration'].sum()
    print("\nTotal travel time is ..", totalTravel)
    print(" Days", totalTravel/86400)

    
    # TO DO: display mean travel time
    meanTravel = df['Trip Duration'].mean()
    print("\nMean travel time is ..", meanTravel)
    print(" Minutes", meanTravel/60)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# def user_stats(df):
#     """Displays statistics on bikeshare users."""

#     print('\nCalculating User Stats...\n')
#     start_time = time.time()

#     # TO DO: Display counts of user types
#     userCounts = df['User Type'].value_counts()
#     print("\nCounts of user types is .." , userCounts)


#     # TO DO: Display counts of gender
#     genderCounts = df['Gender'].value_counts()
#     print("\nCounts of gender is .. " ,genderCounts)


#     # TO DO: Display earliest, most recent, and most common year of birth
#     earliest = df['Birth_Year'].min()
#     print("\nEarliest is .." ,earliest)
#     mostRecent = df['Birth_Year'].max()
#     print("\nMost recent is .." ,mostRecent)
#     mostCommonBirth = df['Birth Year'].mode()[0]
#     print("\nMost common year of birth is .." ,mostCommonBirth)


#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        # user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
