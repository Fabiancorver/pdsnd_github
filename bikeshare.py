import time
import pandas as pd
import numpy as np


#Locate bikeshare city data 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_names = ['chicago', 'new york city', 'washington']
month_names = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
day_names = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

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
    city = input('Which city would you like to select? chicago, new york city or washington? ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print("Oh nooo, this city cannot be found. Please try again!")
        city = input('Which city would you like to select? chicago, new york city or washington? ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month would you like to select? all, january, february, ... , june? ').lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print("Oh nooo, this is not a valid month")
        month = input('Which month would you like to select? all, january, february, ... , june? ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day of the week would you like to select? all, monday, tuesday, ... sunday? ')
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print("This is not a valid day of the week")
        day = input('Which day of the week would you like to select? all, monday, tuesday, ... sunday? ')


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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month)+1

       # filter by month to create the new dataframe
       df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != all:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    frequent_month = df['Start Time'].dt.month.mode()[0]

    # TO DO: display the most common day of week
    frequent_day = df['Start Time'].dt.weekday_name.mode()[0]

    # TO DO: display the most common start hour
    frequent_hour = df['Start Time'].dt.hour.mode()[0]

    print("The Most Frequent Month is %s " % (frequent_month))
    print("The Most Frequent Day is %s " % (frequent_day))
    print("Most Frequent Hour is %s " % (frequent_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    frequent_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    frequent_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip

    trip_with_counts = df.groupby(['Start Station','End Station']).size().reset_index(name = 'trips')

    sort_trips = trip_with_counts.sort_values('trips', ascending = False)

    start_trip = sort_trips['Start Station'].iloc[0]

    end_trip = sort_trips['End Station'].iloc[0]

    print("Most Frequent Start Station is %s " % (frequent_start_station))
    print("Most Frequent End Station is %s " % (frequent_end_station))
    print("Most popular trip is from %s to %s " % (start_trip,end_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_trip_time = df['Trip Duration'].mean()

    print("Total Travel Time is %s in seconds " % (total_trip_time))
    print("Mean Travel Time is %s in seconds " % (mean_trip_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Count's of User Type's ")

    if 'User Type' in df.columns:
        print(df['User Type'].value_counts())
    else:
        print("Oops..! for %s User Type data is not available " % (city))

    # TO DO: Display counts of gender
    print("Count's of Gender ")

    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print("Oops..! for %s Gender data is not available " % (city))

    # TO DO: Display earliest, most recent, and most common year of birth

    print(" Stats regarding Birth Year data ")

    if 'Birth Year' in df.columns:

        max_birth_year = df['Birth Year'].max()

        print("Most Recent Birth Year is %s " % (max_birth_year))

        min_birth_year = df['Birth Year'].min()

        print("Most Earliest Birth Year is %s " % (min_birth_year))

        frequent_birth_year = df['Birth Year'].mode()[0]

        print("Most Frequent Birth Year is %s " % (frequent_birth_year))
    else:
        print("Oops..! for %s Birth Year data is not available " % (city))
    print('-'*100)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        print("Would you like see five rows of data? Enter yes or no ")
        display_data = input()
        display_data = display_data.lower()

        i = 5
        while display_data == 'yes':

            print(df[:i])
            print("Would you like to see five more rows of data? Enter yes or no ")
            i *= 2
            display_data = input()
            display_data = display_data.lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
