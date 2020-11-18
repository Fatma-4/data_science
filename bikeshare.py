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
    months = ('all','january', 'february', 'march', 'april', 'may', 'june')
    days = ('all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday')

    #         city = input('Which of these cities do you want to see data : {} \n>'.format(cities))
    while True:
        city = input('Which of these cities do you want to see data : Chicago , New york city,Washington \n>')
        if city in cities:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter a month to get result {} \n> '.format(months))
        if month in months:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = input('Please enter a day to get result {} \n> '.format(days))
        if day in days:
            break


    print('-'*40)
#     print("city, month, day" + city, month, day)

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

#     fileC=""
#     if city == "chicago":
#         fileC="chicago.csv"
#     if city == "new york city":
#         fileC="new_york_city.csv"
#     if city == "washington":
#         fileC="washington.csv"
# #      df= pd.read_csv(fileC)

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name
    
    
    if month != 'all':
        month =  month.index(month) + 1
        df = df[df['month'] == month]

        
    if day != 'all':
        df = df[ df['day'] == day.title()]
    
    print(day)
    print(month)

    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
