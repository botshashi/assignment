

class DaysPredictor:
    """
    The idea behind the solution is: as we are allowed to miss either 0, 1 or 2 or 3 classes, we solve sub-problems
    (with 1, 2, 3,...n days) in bottoms-up manner.
    Time complexity: O(n) where n is number of days
    Space complexity: O(n) to store solution for sub-problems
    """

    def __init__(self):
        self.__result = ''

    @staticmethod
    def compute_possible_days(days):
        if days == 0:
            return 1
        if days == 1:
            return 2
        if days == 2:
            return 4
        if days == 3:
            return 8
        # base case initialization
        dp = [0] * (days + 1)
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        dp[3] = 8
        # calculating sub-problems by bottoms-up approach
        for i in range(4, days + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

        return dp[days]

    # getting number of ways to attend classes over given number of days
    def total_ways_attending_classes(self, days):
        return self.compute_possible_days(days)

    # getting number of ways to attend classes over given number of days - 1, i.e not attending last class
    def total_ways_missing_ceremony(self, days):
        return self.compute_possible_days(days) - self.compute_possible_days(days-1)

    # getting final result
    def get_result(self, total_num_days):
        self.__result = str(self.total_ways_missing_ceremony(total_num_days)) + '/' + str(self.total_ways_attending_classes(total_num_days))
        return self.__result


if __name__ == '__main__':
    while True:
        user_input = input('Enter number of days: ')
        try:
            total_days = int(user_input)
            if total_days <= 0:
                raise ValueError('Days must be positive integer')
            predictor = DaysPredictor()
            print(f'Answer for {total_days} days: {predictor.get_result(total_days)}')
        except ValueError as e:
            print('Days must be positive integer')
        finally:
            print('Use Ctrl-Z to exit or Continue')