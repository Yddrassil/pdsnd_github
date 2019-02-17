import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days= ['monday', 'tuesday', 'wedneday', 'thursday', 'friday', 'saturday','sunday','all']
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
    while True:
        city=input('Select a city (Chicago, New York City, Washington) ').lower()
        if city in CITY_DATA.keys():
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Enter a month: ').lower()
        if month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Enter a day: ').lower()
        if day in days:
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


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month=int(df['month'].value_counts().argmax())
    print('\nMost common month is: ',months[month-1])

    # TO DO: display the most common day of week
    print('\nMost common day is: ',df['day_of_week'].value_counts().argmax())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('\nMost common start hour is: ',df['hour'].value_counts().argmax())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    start_station=df['Start Station'].value_counts()
    print('\nMost common start station is: ',start_station.argmax())


    # TO DO: display most commonly used end station
    end_station=df['End Station'].value_counts()
    print('\nMost common end station is: ',end_station.idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost common route is: ',df.groupby(['Start Station','End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time= df['Trip Duration'].sum()
    print('Total travel time is ',total_travel_time/60,' hours')

    # TO DO: display mean travel time
    mean=df['Trip Duration'].mean()
    print('\nMean travel time is: ',mean/60,' hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nUser Types \n ',df['User Type'].value_counts())

    while True:
        try:
    # TO DO: Display counts of gender
            print('\nGender\n ',df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
            print('\nEarliest year of birth is',df['Birth Year'].min())
            print('\nMost recent year of birth is',df['Birth Year'].max())
            print('\nMost common year of birth is',df['Birth Year'].value_counts().idxmax())
            break
        except:
            print('\nThere is no gender and birth year data for this city')
            break
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
     """Asks user to display 5 rows of raw data."""
     choice= input('Would you like to see the raw data? ').lower()
     if choice=='yes' or choice=='y':
        i=0
        print(df.iloc[i:i+5])
        while True:
            more= input('Would you like to see additional 5 rows? ').lower()
            if more=='y' or more=='yes':
                i+=5
                print(df.iloc[i:i+5])

            else:
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
  main()
