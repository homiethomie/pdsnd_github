import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january','february','march','april','may','june','all']
DAYS = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

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
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        city = input('Type city: Chicago, New York City, Washington: ').lower()    
        if city not in CITY_DATA:
            print('invalid input, let\'s try again')
            continue
        else:
            time = input('Do you want to filter by month, day, or both? Type \'all\' if no filter should be applied: ').lower()
            if time == 'month':
                month = input('Name of the month to filter by (January, February, March, April, May, or June), or \'all\' to apply no month filter: ').lower()
                day = 'all'
                if month not in MONTHS:
                    print('invalid input, let\'s try again')
                    continue
                else:
                    break
            elif time =='day':
                month = 'all'
                day = input('Name of the weekday to filter by (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday), or \'all\' to apply no weekday filter: ').lower()
                if day not in DAYS:
                    print('invalid input, let\'s try again')
                    continue
                else:
                    break
            elif time =='both':
                month = input('Name of the month to filter by (January, February, March, April, May, or June), or \'all\' to apply no month filter: ').lower()
                if month not in MONTHS:
                    print('invalid input, let\'s try again')
                    continue
                else:
                    day = input('Name of the weekday to filter by (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday), or \'all\' to apply no weekday filter: ').lower()
                    if day not in DAYS:
                        print('invalid input, let\'s try again')
                        continue
                    else:
                        break
            elif time =='all':
                month = 'all'
                day = 'all'
                break
            else:
                print('please check your input. let\'s try again')
                continue
            
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, week, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['weekday'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # redundant: df['month'] = df['Start Time'].dt.month
    #print(df['month'].is_integer())
    #df['month'] = df['month'].astype(int)
    #df.head()
    common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    common_month = months[common_month - 1]
    print('The most popular month is',common_month)
    
    # EXTRA TO DO: display the busiest week
    df['week'] = df['Start Time'].dt.week
    calendar_week = df['week'].mode()[0]
    print('The busiest week was calendar week',calendar_week)
    
    # TO DO: display the most common day of week
    common_day = df['weekday'].mode()[0]
    print('The most common day is',common_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is',common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most common start station is :',start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most common end station is :', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combo Station'] = df["Start Station"] +" - "+ df["End Station"]
    common_combo = df['Combo Station'].mode()[0]
    print('The most frequent combination of start station and end station is :', common_combo)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time is : ',total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The mean travel time is : ',mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    value_counts = df['User Type'].value_counts()
    print('The user type information is: \n',value_counts)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print('The gender type information is: \n',gender_counts)
    else:
        print('In this file is no gender information')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('The earliest, most recent, and most common year of birth (in this order) is: ',earliest, ', ', most_recent, ', ', most_common)
    else:
        print('In this file is no birth year information')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    rows = 0
    answers = ['yes','no']
    while True:
        interest = input('Would you like to see (more) rows of raw data? (Yes or No): ').lower()
        if interest not in answers:
            print('Invalid answer! Let\'s try again with Yes or No')
            continue
        elif interest == 'yes':
            try:
                amount = int(input('How many rows would you like to display?'))
            except ValueError:
                print('Please enter a number. Let\'s try again')
                continue
            if amount > 0:
                print(df.iloc[rows : rows + amount])
                rows += amount
            else:
                print('Invalid input. Let\'s do this again, and enter a number greater than 0')
                continue
        else:
            print('Well then, let\'s move on')
            break
                

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Bye; come again!')
            break


if __name__ == "__main__":
	main()
